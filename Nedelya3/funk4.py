def name_file(a):
    c = open(f'{a}.txt', 'w') 
    c.close()

x = input()
c = name_file(x)
c