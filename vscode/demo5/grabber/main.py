from pathlib import Path

import requests

url = "https://russianwarship.rip"
response = requests.get(url)
Path("index.html").write_bytes(response.content)
print("done\a")
