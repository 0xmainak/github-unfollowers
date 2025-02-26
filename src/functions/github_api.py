import requests
import time
import random

class GithubAPI:
    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"

    def get_paginated_data(self, url):
        headers = {"Authorization": f"token {self.token}"}
        users = set()
        page = 1
        while True:
            response = requests.get(f"{url}?per_page=100&page={page}", headers=headers)
            if response.status_code != 200:
                break
            data = response.json()
            if not data:
                break  # Stop if no more data
            users.update(user['login'] for user in data)
            page += 1
        return users

    def get_following(self):
        return self.get_paginated_data(f"{self.base_url}/users/{self.username}/following")

    def get_followers(self):
        return self.get_paginated_data(f"{self.base_url}/users/{self.username}/followers")

    def unfollow_user(self, username):
        url = f"{self.base_url}/user/following/{username}"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            print(f"Unfollowed {username}")
        else:
            print(f"Failed to unfollow {username}: {response.status_code} - {response.text}")

    def random_sleep(self, min_time, max_time):
        time.sleep(round(random.uniform(min_time, max_time), 2))
