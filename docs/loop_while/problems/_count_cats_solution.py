'''
"Скільки котиків?"

Скільки раз зустрічається слово "котик" в string.
'''
def count_cats(string):
	str_to_find = 'котик'
	str_length = len(str_to_find)
	count = 0
	index = 0
	while index <= len(string) - str_length:
		if string[index:index + str_length] == str_to_find:
			count += 1
			# index += 5
		# else:
		index += 1
	return count
	
assert count_cats('') == 0
assert count_cats('котки') == 0
assert count_cats('котик') == 1
assert count_cats('два гарних котика') == 1
assert count_cats('котиккотик') == 2
assert count_cats('котик і ще один котик') == 2
assert count_cats('           котик котик   котик     котик    котик            ') == 5
