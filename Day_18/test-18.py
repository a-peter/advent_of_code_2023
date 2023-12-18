def berechne_flaeche(vektoren):
    x = [p[0] for p in vektoren]
    y = [p[1] for p in vektoren]
    return 0.5 * abs(sum(x[i-1]*y[i] - x[i]*y[i-1] for i in range(len(vektoren))))

vektoren = [(4, 10), (9, 7), (11, 2), (2, 2)]
# vektoren = [(2, 10), (11, 10), (11, 2), (2, 2)]
flaeche = berechne_flaeche(vektoren)
print(f'Die Fläche beträgt {flaeche}')
