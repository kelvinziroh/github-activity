import json
import pprint

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
        print(f"event id: {event['id']}")
        print(f"event type: {event['type']}")
        print(f"repo: {event['repo']['name']}")
        print(f"public: {event['public']}")
        print(f"created_at: {event['created_at']}\n")


if __name__ == "__main__":
    main()
