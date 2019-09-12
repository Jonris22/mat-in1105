n = int(input('Velg det største tallet du vil ha i listen: '))      #Øvre grense
q = 0                                                               #En vilkårlig variable til while-løkken
liste = []                                                          #En liste til oddetallene
          
while q <= n:                                                       #Kjører så lenge q er mindre eller lik n
    if q % 2 =! 0:                                                  #Denne kjører når q ikke er delelig på 2
        liste += [q]                                                #Legger til q som et ledd i listen liste
    q += 1                                                          #Øker q med 1
                  
print(liste)                                                        #Printer ut listen med oddetall


"""
terminal> python odd.py
    Velg n: 10
    [1, 3, 5, 7, 9]
    
"""