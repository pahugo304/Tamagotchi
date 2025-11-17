from dataclasses import dataclass, asdict


@dataclass
class Tamagotchi:
    name: str
    hunger: int = 20
    energy: int = 80
    mood: int = 80
    cleanliness: int = 80
    age: int = 0

    MIN_VALUE = 0
    MAX_VALUE = 100

    def clamp_stats(self):
        self.hunger = max(self.MIN_VALUE, min(self.hunger, self.MAX_VALUE))
        self.energy = max(self.MIN_VALUE, min(self.energy, self.MAX_VALUE))
        self.mood = max(self.MIN_VALUE, min(self.mood, self.MAX_VALUE))
        self.cleanliness = max(self.MIN_VALUE, min(self.cleanliness, self.MAX_VALUE))

    def is_alive(self) -> bool:
        if self.hunger >= self.MAX_VALUE:
            return False
        if self.energy <= self.MIN_VALUE:
            return False
        if self.mood <= self.MIN_VALUE:
            return False
        if self.cleanliness <= self.MIN_VALUE:
            return False
        return True

    def status_message(self) -> str:
        if not self.is_alive():
            return f"{self.name} ne va pas bien..."
        if self.hunger > 70:
            return f"{self.name} a très faim !"
        if self.energy < 30:
            return f"{self.name} est très fatigué."
        if self.mood < 30:
            return f"{self.name} est déprimé..."
        if self.cleanliness < 30:
            return f"{self.name} est très sale."
        return f"{self.name} est content :)"

    def apply_turn_effects(self):
        self.age += 1
        self.hunger += 8
        self.energy -= 5
        self.mood -= 3
        self.cleanliness -= 4
        self.clamp_stats()


    def feed(self):
        self.hunger -= 20
        self.mood += 5
        self.cleanliness -= 5
        self.clamp_stats()

    def sleep(self):
        self.energy += 30
        self.hunger += 10
        self.cleanliness -= 3
        self.clamp_stats()

    def play(self):
        self.mood += 20
        self.energy -= 10
        self.hunger += 5
        self.cleanliness -= 5
        self.clamp_stats()

    def wash(self):
        self.cleanliness += 30
        self.mood -= 2
        self.clamp_stats()


    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Tamagotchi":
        return cls(**data)
