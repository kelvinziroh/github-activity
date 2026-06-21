import pprint
from datetime import datetime


def render_activity(username: str, activity_log: list, activity_stats: dict[str, int]):
    print(f"{username}'s activity:\n")
    if len(activity_log) == 0:
        print(f"{username} has no recent activity in the last 90 days")
    else:
        for activity in activity_log:
            print(activity)

        print("\nActivity stats:")
        for stat_key, stat_val in activity_stats.items():
            print(f"{[stat_key]}: {stat_val}")

        print(f"\n{username}'s activity logged up to last 90 days")


def get_activity(event_data: list) -> tuple[list, dict[str, int]]:
    activity_log = []
    activity_stats = {
        "PushEvent": 0,
        "WatchEvent": 0,
        "CreateEvent": 0,
        "PullRequestEvent": 0,
        "PullRequestReviewEvent": 0,
        "PullRequestReviewCommentEvent": 0,
        "IssueEvent": 0,
        "IssueCommentEvent": 0,
    }

    for event in event_data:
        type = event["type"]
        repo = event["repo"]
        payload = event["payload"]
        formatted_date = format_date(event["created_at"])
        pr_number = (
            payload["pull_request"]["number"] if "pull_request" in payload else None
        )

        activity_stats[type] += 1

        match type:
            case "PushEvent":
                activity_log.append(
                    f"- [{formatted_date}]: Pushed commit(s) to {repo['name']}"
                )
            case "WatchEvent":
                activity_log.append(f"- [{formatted_date}]: Starred {repo['name']}")
            case "CreateEvent":
                activity_log.append(f"- [{formatted_date}]: Created {repo['name']}")
            case "PullRequestEvent":
                activity_log.append(
                    f"- [{formatted_date}]: {payload['action'].capitalize()} PR #{payload['number']} in {repo['name']}"
                )
            case "PullRequestReviewEvent":
                activity_log.append(
                    f"- [{formatted_date}]: {payload['action'].capitalize()} review on PR #{pr_number} in {repo['name']}"
                )
            case "PullRequestReviewCommentEvent":
                activity_log.append(
                    f"- [{formatted_date}]: Commented on PR #{pr_number} review in {repo['name']}"
                )
            case "IssueEvent":
                activity_log.append(
                    f"- [{formatted_date}]: {payload['action'].capitalize()} an issue in {repo['name']}"
                )
            case "IssueCommentEvent":
                activity_log.append(
                    f"- [{formatted_date}]: Commented on an issue in {repo['name']}"
                )
            case _:
                print(f"event id: {event['id']}")
                print(f"event type: {type}")
                print(f"repo: {repo['name']}")
                print(f"public: {event['public']}")
                print(f"created_at: {formatted_date}\n")

    return activity_log, activity_stats


def format_date(date_str: str) -> str:
    iso_str = date_str.replace("Z", "+00:00")
    dt_utc = datetime.fromisoformat(iso_str)
    dt_local = dt_utc.astimezone()
    return dt_local.strftime("%Y-%m-%d %H:%M:%S%z")
