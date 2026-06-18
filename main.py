import pprint

import requests


def main():
    username = input("Enter username: ")
    response = requests.get(
        f"https://api.github.com/users/{username}/events",
        headers={"accept": "application/vnd.github+json"},
    )
    print(f"{username}'s activity:")
    pprint.pprint(response.text, indent=4)


if __name__ == "__main__":
    main()
