# Задача эйлера 38

def proizv(x):
	rez = ''
	k = 1
	while len(str(rez)) < 9:
		rez += str(x*k)
		k=k+1
	return rez

max_rez =''
max_max = 1
for i in range(9,1000000):
	
	if sorted(proizv(i)) == ['1','2','3','4','5','6','7','8','9']:
		max_rez = int(proizv(i))
		if max_rez > max_max:
			max_max = max_rez
print(max_max)