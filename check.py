import requests

PLATFORMS = {
    "facebook": "https://www.facebook.com/{}",
    "instagram": "https://www.instagram.com/{}",
    "x": "https://x.com/{}",
    "tiktok": "https://www.tiktok.com/@{}",
    "reddit": "https://www.reddit.com/user/{}",
    "linkedin": "https://www.linkedin.com/in/{}",
    "spotify": "https://open.spotify.com/user/{}",
    "quora": "https://www.quora.com/profile/{}",
    "twitch": "https://www.twitch.tv/{}",
    "medium": "https://medium.com/@{}"
}

KEYWORDS = {
    "facebook": ["this page isn't available", "content isn't available"],
    "instagram": ["sorry, this page isn't available"],
    "x": ["this account doesn’t exist", "this account doesn’t exist"],
    "tiktok": ["couldn't find this account"],
    "reddit": ["sorry, nobody on reddit goes by that name"],
    "linkedin": ["profile not found"],
    "spotify": ["page not found"],
    "quora": ["profile not found", "this page doesn’t exist"],
    "twitch": ["sorry. unless you’ve got a time machine"],
    "medium": ["404 not found"]
}

def check_handle_availability(username):
    print(f"\nchecking availability for '{username}':\n")

    for platform, url in PLATFORMS.items():
        try:
            response = requests.get(url.format(username), timeout=5)
            page = response.text.lower()

            if response.status_code == 404:
                print(f"{platform}: available")
            elif platform in KEYWORDS and any(keyword in page for keyword in KEYWORDS[platform]):
                print(f"{platform}: available")
            else:
                print(f"{platform}: taken")

        except requests.RequestException:
            print(f"{platform}: error connecting")

def run(username):
    check_handle_availability(username)
