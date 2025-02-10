import random

nomi = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]
cognomi = ["Stoneforge", "Moonshadow", "Starwhisper", "Thunderbeard", "Fireheart", "Ravenwing", "Icebane", "Stormrider", "Swiftfoot", "Dragonflame", "Shadowcloak", "Ironhammer", "Frostbeard", "Silverleaf", "Goldenshield", "Windrider", "Hawkseye", "Deepstone", "Steelheart", "Oakenshield"]

def ottieni_nome_cognome(giocatore: list[any]) -> str:
    return f"{giocatore[0]} {giocatore[1]}"

def crea_giocatore(stringa_dadi: str) -> list[any]:
    giocatore = []
    giocatore.append(random.choice(nomi))
    giocatore.append(random.choice(cognomi))
    giocatore.append(random.randint(80, 101)) #Vita
    giocatore.append(random.randint(5, 11)) #Scudo
    giocatore.append(stringa_dadi)
    return giocatore

def lancia_dadi(lancia_dadi: str) -> list[int]:
    lista = lancia_dadi.split("d")
    lista_dadi = []
    for _ in range(int(lista[0])):
        lancio = random.randint(1, int(lista[1]))
        lista_dadi.append(lancio)
    return lista_dadi

def attacco(attaccante: list[any], difensore: list[any]):
    attacco_giocatore = lancia_dadi(attaccante[4])
    attacco_giocatore.remove(min(attacco_giocatore))
    attacco_giocatore.remove(max(attacco_giocatore))
    attacco_giocatore = sum(attacco_giocatore)
    print(f"I danni causati a {difensore[0]} sono: {attacco_giocatore}")
    danno_giocatore = (attacco_giocatore - difensore[3])
    if danno_giocatore < 0:
        danno_giocatore == 0
    difensore[2] -= danno_giocatore
    print(f"La vita rimanente di {difensore[0]} è: {difensore[2]}")

def main_loop(giocatore1: list[any], giocatore2: list[any]) -> None:
    turni_trascorsi = 0
    while giocatore1[2] > 0 and giocatore2[2] > 0:
        turni_trascorsi += 1
        print(f"Turno: {turni_trascorsi}")
        attacco(giocatore1, giocatore2)
        if giocatore2[2] <= 0:
            print(f"Il vincitore è: {ottieni_nome_cognome(giocatore1)}!")
            break
        attacco(giocatore2, giocatore1)
        if giocatore1[2] <= 0:
            print(f"Il vincitore è: {ottieni_nome_cognome(giocatore2)}!")
            break

def main():
    giocatore1 = crea_giocatore("6d6")
    giocatore2 = crea_giocatore("4d12")
    main_loop(giocatore1, giocatore2)

main()