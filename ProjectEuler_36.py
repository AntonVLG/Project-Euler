# Задача Эйлера 36


def polin_10(x):# Функция проверики  - явояется ли число полиндромом
	a = []
	y = x
	z = bin(int(x))
	z = z.lstrip('-0b')
	
	if str(y) == str(y[::-1]) and str(z) == str(z[::-1]):
		return True
		


z = [] # Список полиндрома в 10й системе

for i in range(1, 1000000):

	if polin_10(str(i)) == True:
		z.append(i)
		print(i)

print(sum(z))
