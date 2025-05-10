import requests

domain = 'example.com'
api_url = 'https://api.api-ninjas.com/v1/whois?domain={}'.format(domain)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)