'''
"Маркування соків"

Завод з виробництва фруктових соків позначає свою продукцію спеціальними ідентифікаторами. 
Ідентифікатор складається з трьох перших букв назви фрукта і об'ему упакування.
"apple", "500 ml" == "APP500"
"pineapple", "45 ml" == "PIN45"
"passion fruit", "750 ml" == "PASFRU750"
'''
def get_drink_id(item_name, volume):
	# ваш код тут
	juice_label = ''
	for word in item_name.split():
		juice_label += word[:3]
	id = juice_label.upper() + volume.strip(' ml')
	# id = f"{juice_label.upper()}{volume.strip(' ml')}"
	return id

# тести
assert get_drink_id("apple", "500 ml") == "APP500"
assert get_drink_id("pineapple", "45 ml") == "PIN45"
assert get_drink_id("passion fruit", "750 ml") == "PASFRU750"
