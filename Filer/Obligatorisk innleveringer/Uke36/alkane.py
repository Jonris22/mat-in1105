M_C = 12.011                                              #Molarmassen til karbon
M_H = 1.0079                                              #Molarmassen til hydrogen

n = []                                                    #Liste for antall karbon
m = []                                                    #Liste for antall hydrogen

MCH = 0                                                   #Massen til bindingene

def M(n, m):                                              #Definisjon for massen til bindingene
    return n*M_C + m*M_H

for i in range(8):                                        #For-loop som kjører 8 ganger
    n += [i+2]                                            #Legger til i + 2 i listen n
    m += [2*n[i]+2]                                       #Legger til 2*n[i] + 2 i listen m (hvor n[i] er det i'ende steget i listen n)

for a,b in zip(n, m):                                     #En for-loop som kjører for hvert ledd i listene n og m
    MCH = M(a, b)                                         #Kaller på definisjonen M med variablene a og b som er ledd i listene n og m
    print(f'M(C{a}H{b}) = {MCH:.2f} g/mol')               #Printer ut massen med to desimaler

    
"""
terminal> python alkane.py
    M(C2H6) = 30.07 g/mol
    M(C3H8) = 44.10 g/mol
    M(C4H10) = 58.12 g/mol
    M(C5H12) = 72.15 g/mol
    M(C6H14) = 86.18 g/mol
    M(C7H16) = 100.20 g/mol
    M(C8H18) = 114.23 g/mol
    M(C9H20) = 128.26 g/mol

"""