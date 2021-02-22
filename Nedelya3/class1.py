class Nout("Acer", "Asus"):
    def _init_(self, name, processor, operativnapamyat, vdeocart,jestkiidisk, matplata,razmerekrana):
        self.name = name
        self.processor = processor
        self.operativnayapamyat = operativnayapamyat
        self.vdeocart = vdeocart
        self.jestkiidisk = jestkiidisk
        self.matplata = matplata
        self.razmerekrana = razmerekrana

   def dict(self):
       print(self.name, self.processor, self.operativnayapamyat, self.vdeocart, self.jestkiidisk, self.matplata, self.razmerekrana}  

