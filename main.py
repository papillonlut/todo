import os
from rich.theme import Theme
from rich.prompt import Prompt
from rich.console import Console
from rich.progress import Progress

# Paramètre
custom_theme = Theme({
    "info": "blue",
    "warning": "magenta"
})
console = Console(theme=custom_theme)

while True:
    print("""
1. Ajouter une tache
2. Modifier une tache
3. Supprimer une tache
4. Afficher toute les taches
5. Quitter""")

    choice = int(input())

    if choice == 1:
        console.clear()
        print("1. Ajouter une tache")

        name = str(input("Entrer le nom : "))
        desc = str(input("Entrer la description : "))
        endDay = int(input("Entrer le jour de fin (JJ) : "))
        endMonth = int(input("Entrer le mois de fin (MM) : "))
        endYears = int(input("Entrer l'année de fin (AAAA) : "))

        console.clear()

        print(f"""Votre Tache
- Nom: {name}
- Description: {desc}
- Date de debut: Aujourd'hui
- Date de fin: {endDay}/{endMonth}/{endYears}""")

        question = str(input("Est-ce bien cela ? "))

        if question == "non":
            11+11
        elif question == "oui":
            file = open(f"todo-(a-finir)\Tache\{name}", "w") 
            file.write(f"""Votre tache
- Nom: {name}
- Description: {desc}
- Date de debut: Aujourd'hui
- Date de fin: {endDay}/{endMonth}/{endYears}""")
            file.close()
        console.clear()
    elif choice == 2:
        console.clear()
        print("2. Modifier une tache")
        name = str(input("Entrer le nom de la tache à modifier : "))

        console.clear()

        with open(f"todo-(a-finir)/Tache/{name}", "r") as file:
            print(file.read())

        desc = str(input("Entrer la nouvelle description : "))
        endDay = int(input("Entrer le nouveau jour de fin (JJ) : "))
        endMonth = int(input("Entrer le nouveau mois de fin (MM) : "))
        endYears = int(input("Entrer la nouvelle année de fin (AAAA) : "))

        with open(f"todo-(a-finir)/Tache/{name}", "w") as file:
            file.write(f"""Votre tache
- Nom: {name}
- Description: {desc}
- Date de debut: Aujourd'hui
- Date de fin: {endDay}/{endMonth}/{endYears}""")
        print("Tache modifiée avec succès.")
        console.clear()
    elif choice == 3:
        console.clear()
        print("3. Supprimer une tache")

        name = str(input("Entrer le nom de la tache à supprimer : "))

        with open(f"todo-(a-finir)/Tache/{name}", "r") as file:
            print(file.read())

        question = str(input(f"Etes-vous sur de vouloir supprimer {name} : "))

        if question == "oui":
            os.remove(f"todo-(a-finir)/Tache/{name}")
            print("Tache modifiée avec succès.")
        else:
            print("Suppression annulée avec succès.")
        console.clear()
    elif choice == 4:
        console.clear()
        print("4. Afficher toute les taches")
        print(os.listdir("todo-(a-finir)/Tache"))
    elif choice == 5:
        console.clear()
        print("5. Quitter")
        console.clear()
        exit()