# seekfind (sf)

**seekfind** is a command-line OSINT (Open Source Intelligence) tool written in Python. It’s designed to help investigators, hackers, and researchers gather intelligence on targets using publicly available information.

---

## features

-  **WHOIS Lookup** — fetches domain registration and ownership data.
-  **social media username check** — self explanatory. it currently works on on platforms like Instagram, X/Twitter and Facebook.
-  **planned features**:
  - email breach verification
  - IP geolocation
  - reverse IP lookup
  - metadata extraction from files
  - people search / dox toolkit
  - custom scan reports

---

## requirements

- Python 3.8+
- pip
- requirements.txt

---

## installation

```
git clone https://github.com/gbrlprs/seekfind.git
cd seekfind
python -m venv .venv
.venv\Scripts\activate  # for windows
# or:
source .venv/bin/activate  # for macOS or linux

pip install -r requirements.txt
````

## how to use

domain lookup: 
````
python whois_lookup.py -d [website.com]
````
social media username checker: 
````
python social_media_check.py -u [username]
````

---

## notes
- the social media check uses HTTP status codes (200/404) to determine if a username exists.

- WHOIS uses the python-whois module or a custom API integration (e.g., APILayer, WhoisXML, etc.), shout out to them.

- no GUI or web interface—everything happens in the terminal.

---

##  disclaimer
seekfind is for ethical and educational use only. any misuse of this software is the sole responsibility of the user.


## possible contributions
pull requests and feature suggestions are welcome. if you want to fork the repo and help expand sf into a full-spectrum OSINT platform, you are welcome to do so. basically any solid architectural advice for the software is welcome as long as it is presented first through email, you can check it on my profile and i'll be open for messages of the kind.

## built by yours truly — for the anonymous, by the anonymous.

