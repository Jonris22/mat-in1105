from math import exp

def f(B, k, C, t):                                     #Definerer en funksjon for variablene B, k, C og t
    return B/(1 + C*exp(-k*t))                         #Returnerer summen av uttrykket når funksjonen blir kalt på
           
B = 50000                                              #Maksimal befolkning
k = 0.2                                                #Vekstfaktor per time
C = (B/5000) - 1                                       #Startbefolkning
tid = 48                                               #Total tid
N = []                                                 #En liste for antall
           
n = 12                                                 #Antall steg
h = int(tid/n)                                         #Steglengde som integer

t = list(range(0, tid+1, h))                             #Lager en liste fra 0 til og med tid, med steglengde h
         
for i in range(tid+1):                                 #En for-loop som kjører tid + 1 ganger
    N.append(f(B, k, C, i))                            #Kaller på funksjonen f() med gitt verdier
    
print('Tid (h)     Populasjon (stk)')                  #Printer ut kategoriene til variablene
for a,b in zip(t, N):                                 
    print('%-12i%-12i' % (a, b))     

#Jeg har med t = 0, for referanse
    
"""
terminal> python population_table.py
    Tid (h)     Populasjon (stk)
    0           5000
    4           5974
    8           7109
    12          8418
    16          9912
    20          11598
    24          13474
    28          15530
    32          17748
    36          20098
    40          22542
    44          25034
    48          27526

"""