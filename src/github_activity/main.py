import argparse
import sys
from datetime import datetime

import requests

from github_activity.activity import get_activity, render_activity
from github_activity.info import get_info, render_info


def main():
    args = get_args()
    username = args.username

    if args.profile:
        info_data = get_data(f"https://api.github.com/users/{username}")
        if info_data is None:
            sys.exit()
        filtered_info = get_info(info_data)
        render_info(username, filtered_info)
    else:
        activity_data = get_data(f"https://api.github.com/users/{username}/events")
        if activity_data is None:
            sys.exit()
        activity_log, activity_stats = get_activity(activity_data)
        render_activity(username, activity_log, activity_stats)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="The handle for the GitHub user account")
    parser.add_argument(
        "--profile",
        help="Display profile for the GitHub user account",
        action="store_true",
    )

    args = parser.parse_args()
    return args


def get_data(endpoint: str):
    try:
        data = requests.get(
            endpoint,
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
