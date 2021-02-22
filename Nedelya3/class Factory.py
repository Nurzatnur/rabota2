class Factory:
    def _init_(self):
        pass
    def engine(self):
        print("двигатель создан")  
    def bridge(self):
        print("ходовая чать создан")  
fac = Factory()  
fac.engine()
fac.bridge()