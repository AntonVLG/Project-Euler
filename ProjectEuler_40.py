# Задача эйлера 40

x = str()

for i in range(1,200000):
	x += str(i)



a = []
for j in range(len(x)):
	a.append(x[j:j+1])




rez = 1
rez = int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])*int(a[999999])
print(rez)