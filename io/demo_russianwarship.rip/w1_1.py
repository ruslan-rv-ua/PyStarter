import requests
from tabulate import tabulate
from pprint import pprint as pp

# API docs
# https://russianwarship.rip/api-documentation/v2

BASE_URL = 'https://russianwarship.rip/api/v2'
LATEST_STATS_URL = f'{BASE_URL}/statistics/latest'
TERMS_URL = f'{BASE_URL}/terms/ua'

response = requests.get(LATEST_STATS_URL)
# print(response.json())
# data = response.json()
# pp(data)
data = response.json()['data']
# pp(data)
day = data['day']
stats = data['stats']
# pp(stats)
# table = tabulate(stats.items())
# print(table)

terms = requests.get(TERMS_URL).json()['data']
# translated_stats = {terms[k]['title']:v for k,v in stats.items()}
# table = tabulate(translated_stats.items(), tablefmt='plain')
table = tabulate(
    map(lambda key: (terms[key]['title'], stats[key]), stats), 
    tablefmt='plain'
)

print(f'День {day}.')
print(table)