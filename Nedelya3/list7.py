def dict_fun(**kwargs):
    print(tuple(kwargs.keys()))
    printv(tuple(kwargs.values()))

dict_fun(**{'sd21': 22, 'love': 24})