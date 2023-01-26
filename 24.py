def geometra():
    #Area Quadrato:1,Area Rettangolo:2,Area Cerchio:3,Area Triangolo:4

    print("Scegliere la figura")

scelta = int(input('>>>' ))

    #Quadrato

if scelta == 1:
        print("Hai scelto il quadrato")
        lato = int(input('inserire il lato del quadrato >>> '))
        print(f"L'aria del quadrato è {lato*lato}")

    #Rettangolo
elif scelta == 2:
        print("Hai scelto il rettangolo")
        base = float(input('Inserisci il valore della base >>> '))
        altezza = float(input('Inserisci il valore dellaltezza '))
        print(f"L'Area del Rettangolo è {base*altezza}")

    #Cerchio
elif scelta == 3:
        print("Hai scelto il cerchio")
        r = float(input('Inserisci il valore del raggio >>> '))
        print(f"L'area del cerchio è {r*r*3.14}")

    #Triangolo
elif scelta == 4:
        print("Hai scelto il triangolo")
        base = float(input('Inserisci il valore della base >>> '))
        altezza = float(input('Inserisci il valore dellaltezza >>> '))
        print(f"L'Area del Triangolo è {(base * altezza) / 2}")