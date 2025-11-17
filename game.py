from tamagotchi import Tamagotchi
from ascii_art import get_tamagotchi_art
from save_system import save_game, load_game


def print_stats(pet: Tamagotchi) -> None:
    print("=" * 40)
    print(f"Nom : {pet.name} | Âge : {pet.age} tour(s)")
    print(f"Faim       : {pet.hunger}/100")
    print(f"Énergie    : {pet.energy}/100")
    print(f"Humeur     : {pet.mood}/100")
    print(f"Propreté   : {pet.cleanliness}/100")
    print("=" * 40)
    print(pet.status_message())
    print(get_tamagotchi_art(
        pet.hunger, pet.energy, pet.mood, pet.cleanliness, pet.is_alive()
    ))
    print("=" * 40)

    
def ask_action() -> str:
    print("Que voulez-vous faire ?")
    print("1/   Nourrir")
    print("2/  Dormir")
    print("3/   Jouer")
    print("4/  Laver")
    print("5/   Sauvegarder la partie")
    print("6/  Quitter")
    print("\n")
    choice = input("Votre choix :").strip()
    return choice


def game_loop(pet: Tamagotchi) -> None:
    while True:
        print_stats(pet)

        if not pet.is_alive():
            print("GAME OVER... Votre Tamagotchi n'a pas survécu.")
            break

        choice = ask_action()

        if choice == "1":
            pet.feed()
            print(f"Vous nourrissez {pet.name}.")
        elif choice == "2":
            pet.sleep()
            print(f"{pet.name} fait une sieste.")
        elif choice == "3":
            pet.play()
            print(f"Vous jouez avec {pet.name}.")
        elif choice == "4":
            pet.wash()
            print(f"Vous lavez {pet.name}.")
        elif choice == "5":
            save_game(pet)
            print("Partie sauvegardée !")
        elif choice == "6":
            save = input("Voulez-vous sauvegarder avant de quitter ? (o/n) ").strip().lower()
            if save == "o":
                save_game(pet)
                print("Partie sauvegardée !")
            print("À bientôt !")
            print("\n")
            break
        else:
            print("Choix invalide, réessayez.")
            print("\n")
            continue

        pet.apply_turn_effects()


def main():
    print("=== TAMAGOTCHI VIRTUEL ===")
    print("1/ Nouvelle partie")
    print("2/  Charger la partie")
    print("3/   Quitter")
    choice = input("Votre choix : ").strip()

    if choice == "1":
        name = input("Donnez un nom à votre Tamagotchi : ").strip()
        if not name:
            name = "Tama"
        pet = Tamagotchi(name=name)
        game_loop(pet)
    elif choice == "2":
        pet = load_game()
        if pet is None:
            print("Aucune sauvegarde trouvée, démarrage d'une nouvelle partie.")
            name = input("Donnez un nom à votre Tamagotchi : ").strip()
            if not name:
                name = "Tama"
            pet = Tamagotchi(name=name)
        game_loop(pet)
    else:
        print("Au revoir !")


if __name__ == "__main__":
    main()
