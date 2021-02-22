a = 17925 % 17
b = 546 % 17
c = 934 % 17

if a < b and a < c:
	print("little", a, 'a')
if b < a and b < c:
	print("little", b, 'b')
if c < b and c < a:
	print("little", c, 'c')