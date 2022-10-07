# Modul tacka3d:

import math

def unos_tacke (naziv):
    x = float(input(f"Unesite koordinatu x za tacku {naziv}: "))
    y = float(input(f"Unesite koordinatu y za tacku {naziv}: "))
    z = float(input(f"Unesite koordinatu z za tacku {naziv}: "))

    return {
        "x": x,
        "y": y,
        "z": z
    }

def udaljenost (a, b):
    d_x = a['x'] - b['x']
    d_y = a['y'] - b['y']
    d_z = a['z'] - b['z']

    return math.sqrt(d_x ** 2 + d_y ** 2 + d_z ** 2)

def prikazi_tacku (t):
    x = t['x']
    y = t['y']
    z = t['z']

    print(f"({x:.3f}, {y:.3f}, {z:.3f})")

def unos_tacaka (n):
    tacke = []

    for i in range(n):
        t = unos_tacke(f'tacku {i + 1}')
        tacke.append(t)
    
    return tacke

def zabelezi_udaljenosti (ref_t, tacke):
    
    for t in tacke:
        dist = udaljenost(ref_t, t)

        tacka_sa_udaljenoscu = {
            "tacka": t,
            "udaljenost": dist
        }

        return tacka_sa_udaljenoscu

def po_cemu_se_sortira_tacka_sa_udaljenoscu (tacka):
    return tacka['udaljenost']

def sortiraj_tacke_po_udaljenosti (tacka_sa_udaljenoscu):
    tacka_sa_udaljenoscu.sort(key = po_cemu_se_sortira_tacka_sa_udaljenoscu)
    
    return tacka_sa_udaljenoscu