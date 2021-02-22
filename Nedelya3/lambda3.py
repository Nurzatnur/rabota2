def chislo_od(a,n=1):
    if (n>a):
        return
    else:
        print(n,end=' ')
    chislo_od(a,n+2)
