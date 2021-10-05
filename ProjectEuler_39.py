# Задача эйлера 39

import time
from collections import Counter


rez = []

for a in range(1,500):
	for b in range(a,500):
		c = (a**2+b**2)**0.5
		if a+b+c <=1000:
			rez.append(a+b+c)
			
rez1 = Counter(rez)			

print(rez1.most_common(1))
