v = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
d = v.split()
c = []
w = ""
for s in d:
	c.append(s.title())
for t in range(len(c)):
	w = w + c[t]+" "
print(w)
print()