import math

def N(B, k, C, t): #Definerer en funksjon for variablene B, k, C og t
    return B/(1 + C*math.exp(-k*t)) #Returnerer summen av uttrykket når funksjonen blir kalt på

B = 50000 #Maks befolkning
k = 0.2 #Vekstfaktor per time
C = (B/5000) - 1 #Start befolkning
t = 24 #tid i timer

print(f'Etter {t} timer er populasjonen {N(B, k, C, t):.2f}') #N(B, k, C, t) kaller på funksjonen N() med de bestemte variablene


'''
terminal> python population.py
Etter 24 timer er populasjonen 46552.00
'''