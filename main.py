import json
import pprint
from datetime import datetime

import requests


def main():
    username = input("Enter username: ")
    response = requests.get(
        f"https://api.github.com/users/{username}/events",
        headers={"accept": "application/vnd.github+json"},
    ).text
    event_data = json.loads(response)
    print(f"{username}'s activity:")
    for event in event_data:
        if event["type"] == "PushEvent":
            print(
                f"- [{format_date(event['created_at'])}]: Pushed commit(s) to {event['repo']['name']}\n"
            )
        else:
            print(f"event id: {event['id']}")
            print(f"event type: {event['type']}")
            print(f"repo: {event['repo']['name']}")
            print(f"public: {event['public']}")
            print(f"created_at: {format_date(event['created_at'])}\n")


def format_date(date_str: str) -> str:
    iso_str = date_str.replace("Z", "+00:00")
    dt_utc = datetime.fromisoformat(iso_str)
    dt_local = dt_utc.astimezone()
    return dt_local.strftime("%Y-%m-%d %H:%M:%S%z")


if __name__ == "__main__":
    main()
