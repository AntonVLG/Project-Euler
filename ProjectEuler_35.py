# Задача Эйлера 35


import itertools

def perestanovka(x): # Функция перестановки(перебора) цифр в числе
	z = []
	y = str(x)
	for i in range(0,len(y)):
		z.append(int(y[i:i+1]))
	rez = itertools.permutations(z)
	return rez

def soedinenie(x): # Функция соединения списка из цифр в единое число
	y = ''
	for i in x:
		y = y + str(i)
	return int(y)


def prost(x): # Функция проверки простое число или нет
	z = [i for i in range(1, x+1) if x % i == 0]
	if len(z) == 2:
		return True
	else:
		return False





rezt = []
b =[]


k=0

for i in range(0,10000):
	c = 1
	rezt = perestanovka(i)
	for j in rezt:
		if prost(soedinenie(j)) == False:
			c = 0
	if c == 1:
		print(i)
		k=k+1
		b.append(i)


#for g in b:
#	print(g)
print(k)
