from datetime import datetime

import requests


def main():
    username = get_username()
    event_data = get_data(username)
    print(f"{username}'s activity:\n")
    if len(event_data) == 0:
        print(f"{username} has no recent activity in the last 90 days")
    else:
        for event in event_data:
            repo = event["repo"]
            payload = event["payload"]
            if event["type"] == "PushEvent":
                print(
                    f"- [{format_date(event['created_at'])}]: Pushed commit(s) to {repo['name']}"
                )
            elif event["type"] == "WatchEvent":
                print(f"- [{format_date(event['created_at'])}]: Starred {repo['name']}")
            elif event["type"] == "CreateEvent":
                print(f"- [{format_date(event['created_at'])}]: Created {repo['name']}")
            elif event["type"] == "PullRequestEvent":
                if payload["action"] in ["assigned", "unassigned"]:
                    print(
                        f"- [{format_date(event['created_at'])}]: {payload['action'].capitalize()} PR #{payload['number']} to {payload['assignee']} in {repo['name']}"
                    )
                else:
                    print(
                        f"- [{format_date(event['created_at'])}]: {payload['action'].capitalize()} PR #{payload['number']} in {repo['name']}"
                    )
            elif event["type"] == "PullRequestReviewEvent":
                pr_number = payload["pull_request"]["number"]
                print(
                    f"- [{format_date(event['created_at'])}]: {payload['action'].capitalize()} review on PR #{pr_number} in {repo['name']}"
                )
            elif event["type"] == "PullRequestReviewCommentEvent":
                pr_number = payload["pull_request"]["number"]
                print(
                    f"- [{format_date(event['created_at'])}]: Commented on PR #{pr_number} review in {repo['name']}"
                )
            elif event["type"] == "IssueEvent":
                print(
                    f"- [{format_date(event['created_at'])}]: {payload['action'].captialize()} an issue in {repo['name']}"
                )
            elif event["type"] == "IssueCommentEvent":
                print(
                    f"- [{format_date(event['created_at'])}]: Commented on an issue in {repo['name']}"
                )
            else:
                print(f"event id: {event['id']}")
                print(f"event type: {event['type']}")
                print(f"repo: {event['repo']['name']}")
                print(f"public: {event['public']}")
                print(f"created_at: {format_date(event['created_at'])}\n")


def get_username() -> str:
    username = input("Enter username: ")
    return username


def get_data(username) -> list[dict]:
    data = requests.get(
        f"https://api.github.com/users/{username}/events",
        headers={"accept": "application/vnd.github+json"},
    ).json()
    return data


def format_date(date_str: str) -> str:
    iso_str = date_str.replace("Z", "+00:00")
    dt_utc = datetime.fromisoformat(iso_str)
    dt_local = dt_utc.astimezone()
    return dt_local.strftime("%Y-%m-%d %H:%M:%S%z")


if __name__ == "__main__":
    main()
