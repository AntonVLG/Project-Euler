# Задача эйлера 37

def prost(x):
	z = [i for i in range(1, x+1) if x % i == 0]
	if len(z) == 2 or x==1 :
		return True
	else:
		return False




def prov(x):
	y = str(x)
	k = k1 = 0
	for i in range(len(y)):
		z = y[0:i+1]
		#z1 = y[::-1]
		z2 = y[i:]
		#print(z)
		#print(z2)
		if prost(int(z)) == True:
			k = k+1
		if prost(int(z2)) == True:
			k1 = k1+1
	if k == int(len(y)) and k1 == int(len(y)):
		
		#print(k)
		#print(k1)
		return int(x)



a = []
for i in range(10000):
	a.append(prov(i))
b=[n for n in a if n!= None]
for j in b:
	print(j)