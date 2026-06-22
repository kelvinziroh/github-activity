import pprint

import requests


def render_info(username: str, info_data: dict):
    print(f"{username}'s profile:\n")
    for info_key, info_val in info_data.items():
        print(f"[{info_key}]: {info_val}")


def get_info(data: dict) -> dict:
    info_data = {
        "name": data["name"],
        "username": data["login"],
        "location": data["location"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
        "public_repos": data["public_repos"],
        "followers": data["followers"],
        "following": data["following"],
        "profile_url": data["html_url"],
    }

    return info_data
