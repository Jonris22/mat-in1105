from math import pi

g = 9.81 #tyngdeakselerasjonen
rho = 1.2 #lufttetthet
a = 0.11 #radiusen til fotballen
A = pi*(a**2) #Arealet til fotballen
m = 0.43 #Massen til fotballen
C_D = 0.4 #Dragkoeffisienten til en kule
F_g = m*g #tyngdekraften

V = 120 / 3.6 #Farten i m/s for et hardt spark
F_d = 0.5*C_D*rho*A*(V**2) #Luftmotstand under et hardt spark
print(f'Med en fart på {V:.2f} m/s er tyngdekraften {F_g:.1f}N og luftmotstanden {F_d:.1f}N. Ratio av luftmotstand og tyngdekraft: {(F_d/F_g):.1f}')


V = 30 / 3.6 #Farten i m/s for et svakt spark
F_d = 0.5*C_D*rho*A*(V**2) #Luftmotstand under et svakt spark
print(f'Med en fart på {V:.2f} m/s er tyngdekraften {F_g:.1f}N og luftmotstanden {F_d:.1f}N. Ratio av luftmotstand og tyngdekraft: {(F_d/F_g):.1f}')


'''
terminal> python kick.py
Med en fart på 33.33 m/s er tyngdekraften 4.2N og luftmotstanden 10.1N. Ratio av luftmotstand og tyngdekraft: 2.4
Med en fart på 8.33 m/s er tyngdekraften 4.2N og luftmotstanden 0.6N. Ratio av luftmotstand og tyngdekraft: 0.2
'''