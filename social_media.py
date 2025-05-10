import requests
from bs4 import BeautifulSoup

def check_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 404:
        return "not available"
    elif response.status_code == 200:
        return "available"
    else:
        return "error"

def check_twitter(username):
    url = f"https://x.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 404:
        return "not available"
    elif response.status_code == 200:
        return "available"
    else:
        return "error"
    
def check_facebook(username):
    url = f"https://facebook.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 404:
        return "not available"
    elif response.status_code == 200:
        return "available"
    else:
        return "error"

def check_username(username):
    print(f"\nchecking availability for: {username}")
    
    instagram_status = check_instagram(username)
    twitter_status = check_twitter(username)
    facebook_status = check_facebook(username)   
    print("\nusername availability:")
    print(f"Instagram: {instagram_status}")
    print(f"Twitter: {twitter_status}")
    print(f"Facebook: {facebook_status}")

if __name__ == "__main__":
    username = input("enter username: ")
    check_username(username)
