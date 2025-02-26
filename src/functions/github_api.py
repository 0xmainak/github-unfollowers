import requests
import time
import random

class GithubAPI:
    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"

    def get_following(self):
        url = f"{self.base_url}/users/{self.username}/following"
        response = requests.get(url, auth=(self.username, self.token))
        return {user['login'] for user in response.json()} if response.status_code == 200 else set()

    def get_followers(self):
        url = f"{self.base_url}/users/{self.username}/followers"
        response = requests.get(url, auth=(self.username, self.token))
        return {user['login'] for user in response.json()} if response.status_code == 200 else set()

    def unfollow_user(self, username):
        url = f"{self.base_url}/user/following/{username}"
        try:
            response = requests.delete(url, auth=(self.username, self.token))
            if response.status_code == 204:
                print(f"Unfollowed {username}")
            else:
                print(f"Failed to unfollow {username}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error unfollowing {username}: {str(e)}")

    def random_sleep(self, min_time, max_time):
        time.sleep(round(random.uniform(min_time, max_time), 2))