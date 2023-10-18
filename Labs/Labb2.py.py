import matplotlib.pyplot as plt
import math

# Skapa tomma listor för tränings- och testdatapunkter
träning_data = []
test_data = []

# Läs in träningsdata från filen "datapoints.txt" och spara i listan träning_data
with open("datapoints.txt", 'r') as fil:
    for rad in fil:
        delar = rad.strip().split(',')
        if len(delar) == 3:
            bredd, höjd, etikett = map(float, delar)
            träning_data.append((bredd, höjd, int(etikett)))

# Läs in testdata från filen "testpoints.txt" och spara i listan test_data
with open("testpoints.txt", 'r') as fil:
    for rad in fil:
        # Kontrollera att raden följer formatet "(bredd, höjd)"
        if rad.strip().startswith("(") and rad.strip().endswith(")"):
            bredd, höjd = map(float, rad.strip("()").split(','))
            test_data.append((bredd, höjd))

# Plotta träningsdatapunkterna med färger baserat på deras etiketter
x_träning = [punkt[0] for punkt in träning_data]
y_träning = [punkt[1] for punkt in träning_data]
etiketter = [punkt[2] for punkt in träning_data]

plt.scatter(x_träning, y_träning, c=etiketter, cmap='viridis')
plt.xlabel('Bredd')
plt.ylabel('Höjd')

# Funktion för att beräkna avståndet mellan två punkter
def beräkna_avstånd(punkt1, punkt2):
    return math.sqrt((punkt1[0] - punkt2[0])**2 + (punkt1[1] - punkt2[1])**2)

# Användaren matar in en testpunkt
while True:
    try:
        bredd = float(input("Ange bredd för testpunkten: "))
        höjd = float(input("Ange höjd för testpunkten: "))
        break  # Avsluta loopen om inmatningen är korrekt
    except ValueError:
        print("Felaktig inmatning. Ange numeriska värden.")

# Skapa en tupel med användarens input 
användarens_testpunkt = (bredd, höjd)

# Hitta den närmaste träningspunkten till användarens testpunkt
minsta_avstånd = float('inf')
närmaste_etikett = None

for träningspunkt in träning_data:
    avstånd = beräkna_avstånd(användarens_testpunkt, träningspunkt[:2])

    if avstånd < minsta_avstånd:
        minsta_avstånd = avstånd
        närmaste_etikett = träningspunkt[2]

# Klassificera den användardefinierade testpunkten och skriv ut resultatet
klassificering = "Pikachu" if närmaste_etikett == 1 else "Pichu"
print(f"Testpunkt (Bredd, Höjd): ({användarens_testpunkt[0]}, {användarens_testpunkt[1]}) klassificeras som {klassificering}")
print(f"Avstånd till närmaste träningspunkt: {minsta_avstånd}")

# Skriver ut faciten
facit = [
    (25, 32, 1),  # Pikachu
    (24.2, 31.5, 1),  # Pikachu
    (22, 34, 1),  # Pikachu
    (20.5, 34, 0)  # Pichu
]

for bredd, höjd, etikett in facit:
    testpunkt = (bredd, höjd)
    minsta_avstånd = float('inf')
    närmaste_etikett = None

    for träningspunkt in träning_data:
        avstånd = beräkna_avstånd(testpunkt, träningspunkt[:2])

        if avstånd < minsta_avstånd:
            minsta_avstånd = avstånd
            närmaste_etikett = träningspunkt[2]

    klassificering = "Pikachu" if närmaste_etikett == 1 else "Pichu"
    print(f"Exempel med (Bredd, Höjd): ({bredd}, {höjd}) klassificeras som {klassificering}")
    print(f"Avstånd till närmaste träningspunkt: {minsta_avstånd}")

# Visa grafen med träningsdatapunkter och resultat
plt.show()
