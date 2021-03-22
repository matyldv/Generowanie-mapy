import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import colorsys
import numpy as np


def main():
    plik = 'big.dem'
    f = open(plik, "r")
    wymiary = f.readline().split()
    wysokosc = int(wymiary[0])
    szerokosc = int(wymiary[1])
    odleglosc = int(wymiary[2])/100

    dane = []
    for wiersz in f:
        dane.append([float(x) for x in wiersz.split()])
    dane = np.array(dane)

    pt_per_inch = 72
    x = szerokosc / pt_per_inch
    y = wysokosc / pt_per_inch

    plt.figure(figsize=(x, y))


    cdict = {'red': [(0.0, 0.0, 0.0),
                     (0.45, 0.85, 1.0),
                     (1.0, 1.0, 1.0)],

             'green': [(0.0, 1.0, 0.75),
                       (0.45, 1.0, 1.0),
                       (1.0, 0.25, 0.25)],

             'blue': [(0.0, 0.0, 0.0),
                      (0.25, 0.0, 0.0),
                      (1.0, 0.0, 0.0)]}
    mapa = matplotlib.colors.LinearSegmentedColormap('mapa', cdict, 256)
    source = matplotlib.colors.LightSource(azdeg=130, altdeg=45, hsv_min_val=0.65, hsv_max_val=1.0, hsv_min_sat=0.85, hsv_max_sat=1.0)


    map = source.shade(dane,mapa, blend_mode='hsv')
    plt.imshow(map)
    plt.savefig('mapa.pdf')
    plt.show()


if __name__ == '__main__':
    main()
