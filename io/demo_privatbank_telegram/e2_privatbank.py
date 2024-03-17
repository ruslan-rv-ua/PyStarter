# Бібліотека requests:
# pip install requests
# PyPI: https://pypi.org/project/requests/

import requests
import json

# Бібліотека tabulate:
# pip install tabulate
# PyPI: https://pypi.org/project/tabulate/
from tabulate import tabulate

# API курси валют Приватбанка:
# docs: https://api.privatbank.ua/#p24/exchange
URL = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

response = requests.get(URL)
print(f'{response.status_code=}')
print(f'{response.headers['content-type']=}')
print(f'{response.encoding=}')
# print(f'{response.content=}')
# print(f'{response.text=}')
# print(response.json())
text = response.content.decode(response.encoding)
data = json.loads(text)




exit()
print('\n'*5)

if response:
	'''
	for rate in response.json():
		print(f"{rate['base_ccy']}/{rate['ccy']} {rate['buy']} {rate['sale']}")
	'''
	s = tabulate(response.json(), headers='keys')
	print(s)
else:
	print('Error!')