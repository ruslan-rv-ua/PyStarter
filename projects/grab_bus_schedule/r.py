from pathlib import Path
import requests

URL = 'https://mpmr.gov.ua/miski-avtobusni-marsruti.html'

response = requests.get(URL)
Path('page.html').write_text(response.text, encoding='utf8')
