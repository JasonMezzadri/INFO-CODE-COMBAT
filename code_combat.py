import random

vita_personaggio = 30
turni_trascorsi = 0

def lancia_dadi():
    dadi = random.randint(1, 6) 
    return dadi

while True:
    turni_trascorsi += 1
    print(f"Turn: {turni_trascorsi}")
    if vita_personaggio > 0:
        dado = lancia_dadi()
        print(f"Damage Taken: {dado}")
        vita_personaggio -= dado
        print(f"Healt Point: {vita_personaggio}")
        if vita_personaggio <= 0:
            print("The character has been defeated.")
            break