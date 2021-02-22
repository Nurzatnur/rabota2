class Toyota(Factory):
    def _init_(self):
        pass
    def wheels(self):
        print("Колёса готовы")  
    def windows(self):
        print("Стёкла готовы")  
a = list("wheels","windows")