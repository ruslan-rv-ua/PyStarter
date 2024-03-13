# Бібліотека requests:
# pip install requests
# PyPI: https://pypi.org/project/requests/

import requests

# Бібліотека tabulate:
# pip install tabulate
# PyPI: https://pypi.org/project/tabulate/
from tabulate import tabulate

# API курси валют Приватбанка:
# docs: https://api.privatbank.ua/#p24/exchange
URL = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

response = requests.get(URL)
# print(response.status_code)
# print(response.headers['content-type'])
# print(response.encoding)
# print(response.content)
# print(response.text)
# print(response.json())


if response:
	'''
	for rate in response.json():
		print(f"{rate['base_ccy']}/{rate['ccy']} {rate['buy']} {rate['sale']}")
	'''
	print(tabulate(response.json()))
else:
	print('Error!')