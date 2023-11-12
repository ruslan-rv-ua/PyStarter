---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Модуль pprint

Модуль pprint дозволяє у привабливому і читабельному вигляді відображати об'єкты Python. 
При цьому зберігається структура об'єкта і відображення, яке виводить pprint, можна використовувати для створення об'єкта.

### pprint()

Самий простий варіант використання модуля - функція pprint().

Наприклад, список з вкладеними словниками відобразиться так:

students = [{'name':'Johnson John', 'adress': 'Chicago, West ave',  'group': 'A1', 'age': 27, 'marks':[5, 5, 4, 5]},
{'name':'Jamson Jane', 'adress': 'London, Baker street, 221B', 'group': 'A2', 'age': 21, 'marks':[3, 5, 4, 5]},
{'name':'Willson Will', 'adress': 'Kyyiv, Khreschatyk, 26',  'group': 'B2', 'age': 33, 'marks':[5, 3, 4, 5]}]

	:::python
	>>> students = [{'name':'Johnson John', 'adress': 'Chicago, West ave',  'group': 'A1', 'age': 27, 'marks':[5, 5, 4, 5]},
	... {'name':'Jamson Jane', 'adress': 'London, Baker street, 221B', 'group': 'A2', 'age': 21, 'marks':[3, 5, 4, 5]},
	... {'name':'Willson Will', 'adress': 'Kyyiv, Khreschatyk, 26',  'group': 'B2', 'age': 33, 'marks':[5, 3, 4, 5]}]
	>>>
	>>> from pprint import pprint
	>>> pprint(students)
	[{'adress': 'Chicago, West ave',
	  'age': 27,
	  'group': 'A1',
	  'marks': [5, 5, 4, 5],
	  'name': 'Johnson John'},
	 {'adress': 'London, Baker street, 221B',
	  'age': 21,
	  'group': 'A2',
	  'marks': [3, 5, 4, 5],
	  'name': 'Jamson Jane'},
	 {'adress': 'Kyyiv, Khreschatyk, 26',
	  'age': 33,
	  'group': 'B2',
	  'marks': [5, 3, 4, 5],
	  'name': 'Willson Will'}]
	>>>
	
Список списків:

	>>> interfaces = [['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
	... ['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
	... ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]
	>>> pprint(interfaces)
	[['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
	 ['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
	 ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]
	>>>
	
Символьний рядок:

	>>> tunnel = '\ninterface Tunnel0\n ip address 10.10.10.1 255.255.255.0\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source FastEthernet1/0\n tunnel protection ipsec profile DMVPN\n'
	>>>
	>>> pprint(tunnel)
	('\n'
	 'interface Tunnel0\n'
	 ' ip address 10.10.10.1 255.255.255.0\n'
	 ' ip mtu 1416\n'
	 ' ip ospf hello-interval 5\n'
	 ' tunnel source FastEthernet1/0\n'
	 ' tunnel protection ipsec profile DMVPN\n')
	>>>
	
#### Обмеження вкладеності

У функції pprint є додатковий параметр `depth`, який дозволяє обмежувати глибину відображення структури даних.

Наприклад, маємо такий словник:

	>>> result = {
	...    'interface Tunnel0': [' ip unnumbered Loopback0',
	...    ' tunnel mode mpls traffic-eng',
	...    ' tunnel destination 10.2.2.2',
	...    ' tunnel mpls traffic-eng priority 7 7',
	...    ' tunnel mpls traffic-eng bandwidth 5000',
	...    ' tunnel mpls traffic-eng path-option 10 dynamic',
	...    ' no routing dynamic'],
	...    'ip access-list standard LDP': [' deny   10.0.0.0 0.0.255.255',
	...    ' permit 10.0.0.0 0.255.255.255'],
	...    'router bgp 100': {' address-family vpnv4': ['  neighbor 10.2.2.2 activate',
	...        '  neighbor 10.2.2.2 send-community both',
	...        '  exit-address-family'],
	...       ' bgp bestpath igp-metric ignore': [],
	...       ' bgp log-neighbor-changes': [],
	...       ' neighbor 10.2.2.2 next-hop-self': [],
	...       ' neighbor 10.2.2.2 remote-as 100': [],
	...       ' neighbor 10.2.2.2 update-source Loopback0': [],
	...       ' neighbor 10.4.4.4 remote-as 40': []},
	...      'router ospf 1': [' mpls ldp autoconfig area 0',
	...       ' mpls traffic-eng router-id Loopback0',
	...       ' mpls traffic-eng area 0',
	...       ' network 10.0.0.0 0.255.255.255 area 0']}
	>>>
	
Можна відобразити лише ключі, вказавши глибину рівною 1, при цьому приховані рівні вкладеності заміняються на три крапки (`...`):

	>>> pprint(result, depth=1)
	{'interface Tunnel0': [...],
	 'ip access-list standard LDP': [...],
	 'router bgp 100': {...},
	 'router ospf 1': [...]}
	>>>
	
Якщо вказати глибину рівною 2, відобразиться наступний рівень.

### pformat()

Функція `pformat()` не виводить відформатований рядок, а просто повертає його. Це корисно, наприклад, якщо відформатований текст необхідо зберегти у текстовому файлі.

## Додаткові матеріали

Документація Python: [pprint — Data pretty printer](https://docs.python.org/3/library/pprint.html)
