def afiseaza_clauze(clauze, afiseaza=False):
    if not afiseaza:
        return
    if not clauze:
        print("Mulțimea de clauze este goală.")
        return
    for i, clauza in enumerate(clauze, 1):
        print(f"{i}: {set(clauza)}")

def incarca_clauze_din_fisier(nume_fisier):
    multime = set()
    with open(nume_fisier, 'r') as f:
        for linie in f:
            litere = {int(x) for x in linie.strip().split()}
            if litere:
                multime.add(frozenset(litere))
    return multime

def este_tautologie(clauza):
    return any(-lit in clauza for lit in clauza)

def rezolva(ci, cj):
    rezultate = []
    for lit in ci:
        if -lit in cj:
            noua = (ci - {lit}) | (cj - {-lit})
            if not este_tautologie(noua):
                rezultate.append(noua)
    return rezultate

def clauza_unitara(clauza):
    return len(clauza) == 1

def gaseste_unitare(clauze):
    return {next(iter(c)) for c in clauze if clauza_unitara(c)}

def regula_unitare(clauze, afiseaza=False):
    clauze = set(clauze)
    while True:
        unitare = gaseste_unitare(clauze)
        if not unitare:
            break
        for lit in unitare:
            if afiseaza:
                print(f"Aplic regula clauzelor unitare pentru {lit}")
            clauze = {c for c in clauze if lit not in c}
            noi = set()
            for c in clauze:
                if -lit in c:
                    noua = frozenset(l for l in c if l != -lit)
                    if not noua:
                        return {frozenset()}
                    noi.add(noua)
                else:
                    noi.add(c)
            clauze = noi
            afiseaza_clauze(clauze, afiseaza)
    return clauze

def gaseste_litere_pure(clauze):
    toate = set()
    for c in clauze:
        toate.update(c)
    return {lit for lit in toate if -lit not in toate}

def regula_litera_pura(clauze, afiseaza=False):
    clauze = set(clauze)
    while True:
        pure = gaseste_litere_pure(clauze)
        if not pure:
            break
        for lit in pure:
            if afiseaza:
                print(f"Elimin litera pură {lit}")
            clauze = {c for c in clauze if lit not in c}
            afiseaza_clauze(clauze, afiseaza)
    return clauze
