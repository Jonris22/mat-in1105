import numpy.lib.scimath as np

def roots(a, b, c): #definere funksjonen for røttene til et andregrads polynom
    if b**2 - 4*a*c == 0: # om det er dobbel rot
        return (- b + np.sqrt(b**2 - 4*a*c))/(2*a)
    else:
        return (- b + np.sqrt(b**2 - 4*a*c))/(2*a), (- b - np.sqrt(b**2 - 4*a*c))/(2*a)


i = input('Har du et komplekst polynom? ')
if i == 'ja':
    """
    Imaginær delen til røttene blir tillatt til å være lik 0 i en fin utskrift,
    men det gjør ikke real delen, altså er r = 0 + 1i ikke en fin føring mens
    r = 1 + 0i er en godkjent måte å føre på
    """
    a = complex(input('Hva er a?(j for roten av -1) ')) # komplekse polynom har alltid komplekse koeffisienter (R er en delmengde av C)
    b = complex(input('Hva er b?(j for roten av -1) '))
    c = complex(input('Hva er c?(j for roten av -1) '))
    if b**2 - 4*a*c == 0:
        if roots(a, b, c).real == 0:
            print ('%.0fj er den dobbelte roten til det komplekse polynomet' % roots(a, b, c).imag)
        elif roots(a, b, c) < 0:
            print ('%.0f%.0fj er den dobbelte roten til det komplekse polyniomet' % (roots(a, b, c).real, roots(a, b, c).imag))
        else:
            print ('%.0f+%.0fj er den dobbelte roten til det kommplekse polynomet' % ((roots(a, b, c).real, roots(a, b, c).imag)))
    elif roots(a, b, c)[0].real == 0: # røttene er på form r_1 = b_1*i og r_2 = a_2 + b_2*i
        if roots(a, b, c)[0].imag < 0 and roots(a, b, c)[1].imag > 0:
            print ('%.0fj og %.0f+%.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
        elif roots(a, b, c)[0].imag > 0 and roots(a, b, c)[1].imag < 0:
            print ('%.0fj og %.0f%.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
        elif roots(a, b, c)[0].imag < 0 and roots(a, b, c)[1].imag < 0:
            print ('%.0fj og %.0f%.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
        else:
            print ('%.0fj og %0.f+%.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
    elif roots(a, b, c)[1].real == 0: # røttene på form r_1 = a_1 + b_1*i og r_2 = b_2*i  
        if roots(a, b, c)[0].imag < 0 and roots(a, b, c)[1].imag > 0:
            print ('%.0f%.0fj og %.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].imag))
        elif roots(a, b, c)[0].imag > 0 and roots(a, b, c)[1].imag < 0:
            print ('%.0f+%.0fj og %.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].imag))
        elif roots(a, b, c)[0].imag < 0 and roots(a, b, c)[1].imag < 0:
            print ('%.0f%.0fj og %.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].imag))
        else:
            print ('%.0f+%.0fj og %.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].imag))
    else: #røttene er på formen r_1 = a_1 +  b_1*i og r_2 = a_2 + b_2*i
        if roots(a, b, c)[0].imag < 0 and roots(a, b, c)[1].imag > 0:
            print ('%.0f%.0fj og %.0f+%.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
        elif roots(a, b, c)[0].imag > 0 and roots(a, b, c)[1].imag < 0:
            print ('%.0f+%.0fj og %.0f%.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
        elif roots(a, b, c)[0].imag < 0 and roots(a, b, c)[1].imag < 0:
            print ('%.0f%.0fj og %.0f%.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
        else:
            print ('%.0f+%.0fj og %.0f+%.0fj er løsningene på det komplekse polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
else:
    a = float(input('Hva er a? ')) #definerer a,b,c som floats siden et polynom kan ha koeffisienter i R, ikke bare i N
    b = float(input('Hva er b? '))
    c = float(input('Hva er c? '))
    if b**2 - 4*a*c == 0: # for dobbel løsning
        print ('%.2f er den "doble løsningen" til det reelle polynomet' % roots(a, b, c))
    elif b**2 - 4*a*c > 0: # for reell løsning
        print ('%.2f og %.2f er røttene til det reelle polynomet' % (roots(a, b, c)[0], roots(a, b, c)[1]))
    else: # for kompleks løsning.
        """
        Siden røttene er på formen r = a +/- bi, trenger vi ikke å finne hvilken som er positi eller negativ her,
        fordi utifra abc fomelen vil den første imaginærdelen  alltid være positiv og den andre alltid negativ.
        """ 
        if roots(a, b, c)[0].real == 0: # real delen er lik i begge løsningene, og for begrunnelse se string i kompleks avdeling
            print ('%.2fj og %.2fj er løsningene til det reelle polynomet' % (roots(a, b, c)[0].imag, roots(a, b, c)[1].imag))
        else:
            print ('%.2f+%.2fj og %.2f%.2fj er løsningene til det reelle polynomet' % (roots(a, b, c)[0].real, roots(a, b, c)[0].imag, roots(a, b, c)[1].real, roots(a, b, c)[1].imag))
