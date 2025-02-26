from src.functions import GithubAPI
from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if __name__ == "__main__":
    github = GithubAPI(GITHUB_USERNAME, GITHUB_TOKEN)
    
    following = github.get_following()
    followers = github.get_followers()
    
    if following is not None and followers is not None:
        non_followers = following - followers
        
        print(f"Unfollowing {len(non_followers)} users who don't follow back...")
        for user in non_followers:
            github.unfollow_user(user)
            github.random_sleep(1, 3)
    else:
        print("Error: Could not fetch following or followers list")

    print("Done!")