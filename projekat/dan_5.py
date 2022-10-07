# Glavni fajl:

import tacka3d
import misc

def init ():
    ref_t = tacka3d.unos_tacke('referentnu tacku')

    n = misc.unos_u_opsegu("Koliko tacaka cete uneti? ", 1, 10)

    tacke = tacka3d.unos_tacaka(n)

    tacke_sa_udaljenostima = []

    tacka_sa_udaljenoscu = tacka3d.zabelezi_udaljenosti(ref_t, tacke)

    tacke_sa_udaljenostima.append(tacka_sa_udaljenoscu)

    sortirane_tacke = tacka3d.sortiraj_tacke_po_udaljenosti(tacke_sa_udaljenostima)

    tacka3d.prikazi_tacku(sortirane_tacke[0]['tacka'])

init()