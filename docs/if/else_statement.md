---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# else
		
Існує більш складна форма розгалуження: 
if-else. 
Якщо умова при інструкції if виявляється хибною, 
то виконується блок коду при інструкції else. 

	if cash >= total:
		print('Дякуємо за покупку')
		if cash != total:
			change = cash - total
			print('Решта:', change)
	else:
		print('Не вистачає коштів')
	print('До побачення')

Інструкція `else` завжди відноситься до тої інструкції `if`, 
яка має такий самий рівень відступу у початковому коді.

	if cash >= total:
		print('Дякуємо за покупку')
		if cash != total:
			change = cash - total
			print('Решта:', change)
		else:
			print('Без решти')
	else:
		print('Не вистачає коштів')
	print('До побачення')
