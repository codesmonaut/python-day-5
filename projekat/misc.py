# Modul misc:

def unos_u_opsegu (poruka, min_vrednost, max_vrednost):
    n = min_vrednost - 1

    while n < min_vrednost or n > max_vrednost:
        n = int(input(f"{poruka} [{min_vrednost}, {max_vrednost}] "))
    
    return n