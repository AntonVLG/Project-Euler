# Задача Эйлера 34

import math


def prov(x):
	y = str(x)
	z = []
	for i in range(0, len(y)):
		z.append(int(y[i:i+1]))
	rez = 0
	for j in z:
		rez = rez + math.factorial(j)

	return rez



x = []
for i in range(3,1000000):
	if i == prov(i):
		x.append(prov(i))

for i in x:
	print(i)

print('Резульат: ', sum(x))