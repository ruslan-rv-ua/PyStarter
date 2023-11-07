---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Тернарний вираз if-else

Доволі часто зустрічається конструкція наступного вигляду:

	if condition:
		result = expression1
	else:
		result = expression2

Сама по собі конструкція доволі проста, але займає аж 4 рядки коду.
Спеціально для таких випадків в Python є конструкція з більш коротким записом:

	result = expression1 if condition else expression2

Тобто якщо виконується умова condition, 
то a присвоїти значення виразу X, 
інакше a присвоїти значення виразу Y.

Приклад:

	result = 'Good' if answer == right_answer else 'Not good'

Цей код еквівалентний наступному:

	if answer == right_answer:
		result = 'Good'
	else:
		result = 'Not good'
	
