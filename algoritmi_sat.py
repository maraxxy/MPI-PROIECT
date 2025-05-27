import random

# ---------------- Funcții Ajutătoare ----------------

def este_clauza_unitara(clauza):
    return len(clauza) == 1

def gaseste_clauze_unitare(clauze):
    return {next(iter(c)) for c in clauze if este_clauza_unitara(c)}

def regula_clauzelor_unitare(clauze, afiseaza=False):
    clauze = set(clauze)
    while True:
        unitare = gaseste_clauze_unitare(clauze)
        if not unitare:
            break
        for lit in unitare:
            if afiseaza:
                print(f"Aplic regula clauzei unitare cu literalul {lit}")
            clauze = {c for c in clauze if lit not in c}
            clauze_nou = set()
            for c in clauze:
                if -lit in c:
                    clauza_noua = frozenset(l for l in c if l != -lit)
                    if not clauza_noua:
                        return {frozenset()}
                    clauze_nou.add(clauza_noua)
                else:
                    clauze_nou.add(c)
            clauze = clauze_nou
    return clauze

def gaseste_literaluri_pure(clauze):
    toate = set()
    for clauza in clauze:
        toate.update(clauza)
    return {l for l in toate if -l not in toate}

def regula_literalurilor_pure(clauze, afiseaza=False):
    clauze = set(clauze)
    while True:
        pure = gaseste_literaluri_pure(clauze)
        if not pure:
            break
        for lit in pure:
            if afiseaza:
                print(f"Aplic regula literalului pur pentru {lit}")
            clauze = {c for c in clauze if lit not in c}
    return clauze

def rezolva(c1, c2):
    rezultat = []
    for l in c1:
        if -l in c2:
            noua = (c1 - {l}) | (c2 - {-l})
            if not tautologie(noua):
                rezultat.append(noua)
    return rezultat

def tautologie(clauza):
    return any(-l in clauza for l in clauza)

def alegere_literal(clauze, metoda="primul"):
    if metoda == "primul":
        for clauza in clauze:
            for l in clauza:
                return l
    else:
        toate = {l for c in clauze for l in c}
        return random.choice(list(toate))

# ---------------- Algoritmi SAT ----------------

def rezolutie(clauze, afiseaza=False):
    clauze = [frozenset(c) for c in clauze]
    contor = 1

    if afiseaza:
        for c in clauze:
            print(f"{contor}: {set(c)}")
            contor += 1

    while True:
        noi = set()
        existente = set(clauze)

        if not clauze:
            print("SATISFIABIL")
            return True

        perechi = [(clauze[i], clauze[j]) for i in range(len(clauze)) for j in range(i + 1, len(clauze))]

        for c1, c2 in perechi:
            rezolvente = rezolva(c1, c2)
            for r in rezolvente:
                r = frozenset(r)
                if not r:
                    if afiseaza:
                        print(f"({contor}) {{}} din {set(c1)} și {set(c2)}")
                    print("NESATISFIABIL")
                    return False
                if r not in existente and r not in noi:
                    if afiseaza:
                        print(f"{contor}: {set(r)} din {set(c1)} și {set(c2)}")
                    noi.add(r)
                    contor += 1

        if not noi:
            if afiseaza:
                print("\nNicio rezolventă nouă de adăugat")
            print("SATISFIABIL")
            return True

        clauze.extend(noi)

def algoritm_dp(clauze, afiseaza=False):
    if afiseaza:
        for i, c in enumerate(clauze):
            print(f"{i+1}: {set(c)}")

    clauze = regula_clauzelor_unitare(clauze, afiseaza)
    if clauze == {frozenset()}:
        print("NESATISFIABIL")
        return False

    clauze = regula_literalurilor_pure(clauze, afiseaza)
    if clauze == {frozenset()}:
        print("NESATISFIABIL")
        return False

    if not clauze:
        print("SATISFIABIL")
        return True

    if afiseaza:
        print("Nu se mai pot aplica reguli DP, folosesc rezoluție...")
    return rezolutie(clauze, afiseaza)

def dpll(clauze, divizari=0, afiseaza=False):
    clauze = regula_clauzelor_unitare(clauze, afiseaza)
    if frozenset() in clauze or clauze == {frozenset()}:
        if afiseaza:
            print("NESATISFIABIL (conține clauză vidă)")
        return False, divizari

    if not clauze:
        if afiseaza:
            print("SATISFIABIL (nicio clauză rămasă)")
        return True, divizari

    clauze = regula_literalurilor_pure(clauze, afiseaza)
    if not clauze:
        if afiseaza:
            print("SATISFIABIL (litere pure)")
        return True, divizari

    if afiseaza:
        print("Nu se mai pot aplica reguli simple, se face ramificare...")

    # Alegerea unui literal
    lit = alegere_literal(clauze)
    if afiseaza:
        print(f"Ramific pe literalul {lit}")

    # Incrementăm numărul de divizări atunci când facem o alegere de literal
    divizari += 1

    # Crearea celor două ramuri ale căutării
    c1 = clauze | {frozenset({lit})}
    satisfiabil, d = dpll(c1, divizari, afiseaza)
    if satisfiabil:
        return True, d

    c2 = clauze | {frozenset({-lit})}
    return dpll(c2, divizari, afiseaza)

def dpll_cu_afisare(clauze, afiseaza=False):
    if afiseaza:
        print("Pornesc algoritmul DPLL...")
    rezultat, divizari = dpll(clauze, 0, afiseaza)
    if rezultat:
        print("SATISFIABIL")
    else:
        print("NESATISFIABIL")
    if afiseaza:
        print(f"Număr total de divizări: {divizari}")
