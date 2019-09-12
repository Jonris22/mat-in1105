s = 0                         #Summen for for-loop
M = 3                         #Øvre grense for for-loop

for k in range(M):            #Programmet brukte i som variabel her og k i linjen under
    s += 1/((2*(k+1))**2)       #Programmet manglet innrykk og formaterte formelen feil

    
q = 1                         #Vilkårlig variabel
t = 0                         #Summen for while-loop

while q <= M:                 #While-loop som kjører mens q er mindre eller lik M
    t += 1/((2*q)**2)         #Legger til en verdi som er avhengig av q for hver gang loop'en kjører
    q += 1                    #Legger til 1 i q for hver gang loop'en kjører
    
                              #Printer ut begge summene:
print(f'''                    
For-loop:   {s}               

While-loop: {t}
''')


"""
terminal> python sum_for.py

For-loop:   0.3402777777777778

While-loop: 0.3402777777777778

"""