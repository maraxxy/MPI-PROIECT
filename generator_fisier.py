import random


def genereaza_clauze(numar_clauze, numar_litere):
    clauze = []
    for _ in range(numar_clauze):
        numar_litere_clauza = random.randint(2, numar_litere)
        clauza = {random.choice(range(1, numar_litere + 1)) * random.choice([-1, 1]) for _ in
                  range(numar_litere_clauza)}
        clauze.append(clauza)
    return clauze


def salveaza_fisierul(clauze, nume_fisier):
    with open(nume_fisier, 'w') as f:
        for clauza in clauze:
            f.write(" ".join(map(str, clauza)) + " 0\n")


def genereaza_fisier(numar_clauze, numar_litere, nume_fisier):
    clauze = genereaza_clauze(numar_clauze, numar_litere)
    salveaza_fisierul(clauze, nume_fisier)
    print(f"Fișierul {nume_fisier} a fost generat cu {numar_clauze} clauze.")


def imparte_fisier(fisier_intrare, numar_clauze_pe_fisier):
    with open(fisier_intrare, 'r') as f:
        clauze = f.readlines()

    numar_fisier = 1
    for i in range(0, len(clauze), numar_clauze_pe_fisier):
        nume_fisier = f"clauze_{numar_fisier}.txt"
        with open(nume_fisier, 'w') as f_out:
            f_out.writelines(clauze[i:i + numar_clauze_pe_fisier])
        numar_fisier += 1
        print(f"Fișierul {nume_fisier} a fost generat.")


# Exemplu de folosire
genereaza_fisier(10000, 10, "clauze_10000.txt")
imparte_fisier("clauze_10000.txt", 1000)
