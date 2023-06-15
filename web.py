import requests
r = requests.get("https://google.com")
if r.ok:
    print("Your internet works!")
else:
    print("Your internet is broken :(")
