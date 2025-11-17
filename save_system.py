import json
from typing import Optional
from tamagotchi import Tamagotchi

DEFAULT_SAVE_FILE = "save_tamagotchi.json"


def save_game(pet: Tamagotchi, filename: str = DEFAULT_SAVE_FILE) -> None:
    data = pet.to_dict()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_game(filename: str = DEFAULT_SAVE_FILE) -> Optional[Tamagotchi]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Tamagotchi.from_dict(data)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
