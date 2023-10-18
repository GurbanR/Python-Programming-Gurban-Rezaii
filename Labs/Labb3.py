import math  ## importerar modulen math för matematiska beräkningar

class Cirkel: # Skapar Klass cirkel
    def __init__(self, x, y, radie):
        # Initierar x- och y-koordinater samt radie.
        self.x = x
        self.y = y
        self.radie = radie

    def förflytta(self, dx, dy):
        # Kontrollera att dx och dy är numeriska värden
        if type(dx) not in (int, float) or type(dy) not in (int, float):#Kontrollerar om både dx och dy är numeriska 
            raise ValueError("numeriska värden !!.") # felmeddelande om något av dem inte är numeirska

        # Metod för att flytta x och y.
        self.x += dx
        self.y += dy

    @property  ## Property som beräknar cirkelns area och retunerar den.
    def area(self):
        return math.pi * self.radie**2

    @property  ## Property som beräknar cirkelns omkrets och retunerar den
    def omkrets(self):
        return 2 * math.pi * self.radie

    def är_enhetscirkel(self): ##Metod som kontrollerar om cirkeln är en enhetscirkel
        return self.radie == 1

    def är_punkt_inuti(self, punkt_x, punkt_y):# Metod som kontrollerar om en given punkt är inuti cirkeln
        avstånd = math.sqrt((punkt_x - self.x)**2 + (punkt_y - self.y)**2)
        return avstånd <= self.radie

    def __eq__(self, annan): ## Override för att jämföra om två cirklar har samma area.
        return self.area == annan.area

    def __lt__(self, annan):##  Jämföra om cirkeln har mindre area än en annan cirkel.
        return self.area < annan.area

    def __repr__(self):  # Generera en strängrepresentation av cirkeln.
        return f'Cirkel(x={self.x}, y={self.y}, radie={self.radie})'

    def __str__(self): #generera läsbar strängrepresentation av cirkeln.
        return f'Cirkel vid ({self.x}, {self.y})'

class Rektangel: # SKapar Rektangel klass
    def __init__(self, x, y, sida1, sida2):# initierar x och y samt längden av de två sidorna
        self.x = x
        self.y = y
        self.sida1 = sida1
        self.sida2 = sida2

    def förflytta(self, dx, dy): ### Metod för att flytta x och y
        # Kontrollera att dx och dy är numeriska värden
        if type(dx) not in (int, float) or type(dy) not in (int, float): ## 
            raise ValueError("Numeriska värden !!.")

        self.x += dx
        self.y += dy

    @property ## beräknar rektangelns area och returnerar den.
    def area(self):
        return self.sida1 * self.sida2

    @property
    def omkrets(self): ## som beräknar rektangelns omkrets och returnerar den
        return 2 * (self.sida1 + self.sida2)

    def är_kvadrat(self): # # Metod som kontrollerar om rektangeln är en kvadrat
        return self.sida1 == self.sida2

    def är_punkt_inuti(self, punkt_x, punkt_y): ## kontrollerar om en given punkt är inuti rektangeln.
        vänster = self.x - self.sida1 / 2
        höger = self.x + self.sida1 / 2
        överkant = self.y + self.sida2 / 2
        underkant = self.y - self.sida2 / 2
        return vänster <= punkt_x <= höger and underkant <= punkt_y <= överkant

    def __eq(self, annan):# jämföra om två rektanglar har samma area
        return self.area == annan.area

    def __lt(self, annan):# Jämföra om rektangeln har mindre area än en annan rektangel
        return self.area < annan.area

    def __repr__(self): #  en strängrepresentation av rektangeln
        return f'Rektangel(x={self.x}, y={self.y}, sida1={self.sida1}, sida2={self.sida2})'

    def __str__(self): # läsbar strängrepresentation av rektangeln
        return f'Rektangel vid ({self.x}, {self.y})'

