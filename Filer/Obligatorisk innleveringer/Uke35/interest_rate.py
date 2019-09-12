def bank(A, p, n): #Lager en definisjon som trenger argumentene A, p og n
    return A*(1 + p/100)**n #Returnerer summen av uttrykket når funksjonen blir kalt på

A = 1000 #Definerer startsummen som 1000 Euro
p = 5 #Definerer rentene som 5%
n = 3 #Definerer antall år som 3

print(f'Etter {n}år vil summen ha økt med {(bank(A, p, n) - A):.2f} Euro') #bank(A, p, n) kaller på funksjonen bank() med de bestemte variablene


'''
terminal> python interest_rate.py
Etter 3år vil summen ha økt med 157.63 Euro
'''