e = 'Прошли те времена, когда компьютер был грязно-белой офисной коробкой'
d = e.split()
r = len(d)
for g in range(r // 2):
	print(d[g].lower(), end = " ")
s = r-r//2
while s < r:
	print(d[s].upper(), end = " ")
	s += 1
print()