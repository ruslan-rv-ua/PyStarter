import re

pattern = r'(йшов|біг) собі (кіт|пес).'

m = re.match(pattern, 'йшов собі пес.')
m = re.match(pattern, 'йшов собі кіт.')
m = re.match(pattern, 'Біг собі кіт.', flags=re.I)
