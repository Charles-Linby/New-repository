import urllib.request
import json

url = "https://api.github.com/users/torvalds"
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())
    print(data["followers"])