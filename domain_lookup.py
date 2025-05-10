import requests

API_KEY = "XBoF7BC3fViPYooNTEwm1w==xkhKI2AHvt6pQZkm"

def run_whois(domain):
    url = f"https://api.api-ninjas.com/v1/whois?domain={domain}"
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("\nwho they are: ")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("\nerror:", response.status_code)
        print("message:", response.text)

if __name__ == "__main__":
    domain = input("enter domain: ")
    run_whois(domain)
