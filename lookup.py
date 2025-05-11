import requests

API_KEY = "XBoF7BC3fViPYooNTEwm1w==xkhKI2AHvt6pQZkm"

def run(domain: str):
    url = f"https://api.api-ninjas.com/v1/whois?domain={domain}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print("\nerror:", e)
        return

    data = response.json()
    print("\nwho they are:\n")
    for key, value in data.items():
        print(f"{key}: {value}")
