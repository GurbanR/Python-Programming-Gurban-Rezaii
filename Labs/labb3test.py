from Labb3 import Cirkel, Rektangel

cirkel1 = Cirkel(x=0, y=0, radie=1) 
cirkel2 = Cirkel(x=1, y=1, radie=1)
rektangel = Rektangel(x=0, y=0, sida1=1, sida2=1)

print(cirkel1 == cirkel2) 
print(cirkel1.är_punkt_inuti(0.5, 0.5)) 
cirkel1.förflytta(5, 5)
print(cirkel1.är_punkt_inuti(0.5, 0.5)) 

try:
    cirkel1.förflytta("Ger felmeddelanden!!", 5)
except ValueError as e:
    print(e)
