def last():
    list=[1,2,3,4,5,6]
    m= len(list)//2 #делим лист по длину
    print(sorted(list[:m],reverse=True) + sorted(list[m:],reverse=True))
    #сортировать лист по убыванию до и после середину
last()