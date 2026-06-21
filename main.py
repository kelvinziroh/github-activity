import argparse
from datetime import datetime

import requests

from activity import get_activity, render_activity


def main():
    username = get_username()
    event_data = get_data(username)
    if event_data is not None:
        activity_log, activity_stats = get_activity(event_data)
        render_activity(username, activity_log, activity_stats)


def get_username() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="The handle for the GitHub user account")
    args = parser.parse_args()
    return args.username


def get_data(username: str) -> list[dict] | None:
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


if __name__ == "__main__":
    main()
