import requests

def run(email):
    url = f"https://xposedornot-api.com/api/v1/breach/{email}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data.get("breached"):
            print(f"Email {email} has been found in the following breaches:")
            
            # Assuming the 'breaches' key holds a list of breaches
            for breach in data.get("breaches", []):
                # Make sure to handle each breach element properly
                if isinstance(breach, dict):
                    # Printing breach name and date if present in the response
                    print(f"- {breach.get('name', 'Unknown breach')} ({breach.get('breach_date', 'Unknown date')})")
                else:
                    print("Error: Unexpected data format in breach list.")
        else:
            print(f"Email {email} has not been found in any breaches.")
    else:
        print("Error: Unable to check email breach status.")
        print("Status code:", response.status_code)
