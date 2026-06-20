import argparse
from datetime import datetime

import requests


def main():
    username = get_username()
    event_data = get_data(username)
    if event_data is not None:
        render_activity(username, event_data)


def render_activity(username: str, event_data: list):
    print(f"{username}'s activity:\n")
    if len(event_data) == 0:
        print(f"{username} has no recent activity in the last 90 days")
    else:
        for event in event_data:
            type = event["type"]
            repo = event["repo"]
            payload = event["payload"]
            formatted_date = format_date(event["created_at"])
            pr_number = (
                payload["pull_request"]["number"] if "pull_request" in payload else None
            )

            if type == "PushEvent":
                print(f"- [{formatted_date}]: Pushed commit(s) to {repo['name']}")
            elif type == "WatchEvent":
                print(f"- [{formatted_date}]: Starred {repo['name']}")
            elif type == "CreateEvent":
                print(f"- [{formatted_date}]: Created {repo['name']}")
            elif type == "PullRequestEvent":
                print(
                    f"- [{formatted_date}]: {payload['action'].capitalize()} PR #{payload['number']} in {repo['name']}"
                )
            elif type == "PullRequestReviewEvent":
                print(
                    f"- [{formatted_date}]: {payload['action'].capitalize()} review on PR #{pr_number} in {repo['name']}"
                )
            elif type == "PullRequestReviewCommentEvent":
                print(
                    f"- [{formatted_date}]: Commented on PR #{pr_number} review in {repo['name']}"
                )
            elif type == "IssuesEvent":
                print(
                    f"- [{formatted_date}]: {payload['action'].capitalize()} an issue in {repo['name']}"
                )
            elif type == "IssueCommentEvent":
                print(f"- [{formatted_date}]: Commented on an issue in {repo['name']}")
            else:
                print(f"event id: {event['id']}")
                print(f"event type: {type}")
                print(f"repo: {repo['name']}")
                print(f"public: {event['public']}")
                print(f"created_at: {formatted_date}\n")


def get_username() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="The handle for the GitHub user account")
    args = parser.parse_args()
    return args.username


def get_data(username) -> list[dict] | None:
    try:
        data = requests.get(
            f"https://api.github.com/users/{username}/events",
            headers={"accept": "application/vnd.github+json"},
        )
        data.raise_for_status()
        return data.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}")


def format_date(date_str: str) -> str:
    iso_str = date_str.replace("Z", "+00:00")
    dt_utc = datetime.fromisoformat(iso_str)
    dt_local = dt_utc.astimezone()
    return dt_local.strftime("%Y-%m-%d %H:%M:%S%z")


if __name__ == "__main__":
    main()
