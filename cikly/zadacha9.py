a = -100
a1 = a
n = 0
n1 = 0
while a  <= 100:
	if (a % 13 == 0) and (a % 2 == 0):
		print(a, a ** 2)
		n1 += 1
	a += 1
print(n1)
while a1 < 100:
	if a1 % 2 == 1:
		n +=1
		print(a1)
	a1 += 7
print(n)