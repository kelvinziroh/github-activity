import argparse
from datetime import datetime

import requests

from activity import get_activity, get_data, render_activity


def main():
    username = get_username()
    activity_data = get_data(username)
    if activity_data is not None:
        activity_log, activity_stats = get_activity(activity_data)
        render_activity(username, activity_log, activity_stats)


def get_username() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="The handle for the GitHub user account")
    args = parser.parse_args()
    return args.username


if __name__ == "__main__":
    main()
