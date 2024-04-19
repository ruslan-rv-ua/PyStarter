from pathlib import Path

import requests

url = "https://russianwarship.rip"
text = requests.get(url=url).text
Path("index.html").write_text(text, encoding="utf8")
print("done")
