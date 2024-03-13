def hanoi(n, s1, s2, s3):
	if n == 1:
		print(s1, '-', s3)
	else:
		hanoi(n-1, s1, s3, s2)
		print(s1, '-', s3)
		hanoi(n-1, s2, s1, s3)

def hanoi(n, s1, s2, s3):
	if n > 0:
		hanoi(n-1, s1, s3, s2)
		print(s1, '-', s3)
		hanoi(n-1, s2, s1, s3)
		
hanoi(3, '1', '2', '3')
print()
		
def hanoi(n, from_, temp, to_):
	if n == 1:
		print(f'{from_} - {to_}')
	else:
		hanoi(n-1, from_, to_, temp)
		print(f'{from_} - {to_}')
		hanoi(n-1, temp, to_, from_)
		
def hanoi(n, from_, to_, temp):
	if n > 0:
		hanoi(n-1, from_=from_, temp=to_, to_=temp)
		print(f'{from_} → {to_}')
		hanoi(n-1, from_=temp, temp=from_, to_=to_)
		
hanoi(3, from_='1', temp='2', to_='3')