g = 9.81                                          #Tyngdeakselerasjonen
t = []                                            #En liste over tidspunkt
y = []                                            #En liste over avstand

v_0 = 18                                          #Startfarten
t_max = 2*v_0/g                                   #Øvre grense for tiden
n = 10                                            #Antall steg - 1

def f(t):                                         #En funksjon for avstand ved tidspunkt t
    return v_0*t - 0.5*g*t**2

h = t_max/n                                       #Steglengde

for i in range(n+1):                              #En for-løkke som kjører n + 1 ganger
    t.append(h*i)                                 #Legger til h*i i listen t

for i in range(n+1):                              #En for-løkke osm kjører n + 1 ganger
    y.append(f(t[i]))                             #Kaller på funksjonen f for hvert punkt i listen t og legger det inn i listen y
    
print('Tid (s)     Avstand (m)')                  #Printer kategoriene til variablene
for a,b in zip(t,y):                              #En for-løkke som kjører for alle verdiene i listene t og y
        print(f'{a:.2f}        {b:.2f}')          #Printer ut alle verdiene i listene t og y, med to desimaler

        
"""
terminal> python ball_table2.py
    Tid (s)     Avstand (m)
    0.00        0.00
    0.37        5.94
    0.73        10.57
    1.10        13.87
    1.47        15.85
    1.83        16.51
    2.20        15.85
    2.57        13.87
    2.94        10.57
    3.30        5.94
    3.67        0.00

"""