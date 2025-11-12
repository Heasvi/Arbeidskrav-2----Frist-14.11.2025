"""
Oppg 1) Du skal her lage et program som skal starter med
alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive
svaret til skjerm med passende tekst."

"""
from datetime import datetime

#Gir input på året man er født
født = int(input("Hvilket år er du født? "))


#Tar utgangspunkt i året i år. Vil da være generisk og fungere neste år og
år = datetime.now().year

#Regner ut alderen din
alder = år - født

print(f"Du skrev du ble født i {født}, det vil si at du nå er {alder} år gammel.")

#%%

"""
Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe
5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?

"""
import math


#Gir input på hvor mange elever det er 
antall_elever = int(input("Hvor mange elever kommer? "))

#Sjekker om det er en rest etter at man har delt antall elever på 4.
#-er det en rest runder man opp til nærmeste integer. Hvis ikke, tar man bare heltallet som en int
if antall_elever % 4 != 0:
    print(f"Du må kjøpe {math.ceil(antall_elever/4)} pizzaer")
else: 
    print(f"Du må kjøpe {int(antall_elever/4)} pizzaer!")


#%%

"""
Oppg 3) Lag et program med en funksjon som regner om fra grader til radianer.
Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415...

"""

import numpy as np

v_grad = float(input("Skriv in antall grader (0-360): "))

radianer = v_grad * (np.pi/180)

print(f"Du skrev inn {v_grad:.0f} grader, det er {radianer:.2f} radianer.")


#%%

"""
Oppg 4)
a) Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.

b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
Programmet skal på bakgrunn av dette skrive ut følgende setning:
London er hovedstaden i England og det er 8.982 mill. innbyggere i London

c) Lag et program som ber brukeren skrive inn info om et nytt land (altså et land som
ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm
"""

#a)
data = {"Norge":["Oslo", 0.634], "England":["London", 8.982],"Frankrike":["Paris", 2.161],"Italia":["Roma", 2.873]}


#b)

INPUT = str(input("Skriv inn et av landene i lista for å få mer informasjon: "))
print("\n")

if INPUT in data:
    hovedstad, antall = data[INPUT]
    print (f"{hovedstad} er hovedstaden i {INPUT}, det er {antall}. mill innbyggere i {hovedstad}.")
else:
    print("Beklager, noe gikk galt, sjekk stavemåten feks, stor forbokstav og ellers små")

print("\n")

nytt_land= str(input("Skriv nå inn informasjon om et nytt land som skal inn i lista, skriv inn land: "))
ny_hovedstad = str(input("Skriv inn navnet på hovedstaden: "))
antall_innbyggere = float(input("Skriv inn antall innbyggere i hovedstaden: "))


data[nytt_land] = [ny_hovedstad,antall_innbyggere]

print("\n")
print(f"Oppdatert liste vil nå være: {data}")

    

#%%

"""
Oppg 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
tekst.
    
"""
import math
import numpy as np

a= float(input("Skriv inn lengden på a: "))

b = float(input("Skriv inn lengden på b: "))

areal_halvsirkel = (np.pi*a**2)/2 

hypotenus = math.sqrt(a**2 + b**2)

areal_trekant = (a * b)/2

omkrets_halvsirkel = (2*np.pi*a)/2

areal_tot = areal_halvsirkel + areal_trekant

omkrets_tot = omkrets_halvsirkel + b + hypotenus

print(f"Totalt areal er {areal_tot:.3f} og total omkrets er {omkrets_tot:.3f}")


#%%%

"""
Oppg 6) Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥^2 − 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
[-10,10]
"""

import numpy as np 
import matplotlib.pyplot as plt

x= np.linspace(-10,10,200)

funksjon = -(x**2) - 5

plt.plot(x,funksjon)
plt.title("Plot av funksjonen f(x) i intervallet [-10,10]")
plt.grid(True)
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.axhline(0,xmin = -15, xmax= 15)
plt.axvline(0)
plt.show()




































