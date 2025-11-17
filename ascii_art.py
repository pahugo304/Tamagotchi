def get_tamagotchi_art(hunger: int, energy: int, mood: int, cleanliness: int, alive: bool) -> str:
    if not alive:
        return r"""
        xxxxxxxxxxxxx
        x   R.I.P   x
        x  (x   x)  x
        x    ---    x
        xxxxxxxxxxxxx
        """

    if mood > 70 and hunger < 50 and energy > 50 and cleanliness > 50:
        return r"""
          /\_/\ 
         ( ^.^ )
          > ^ <
        """
    elif mood < 30 or energy < 30 or cleanliness < 30 or hunger > 70:
        return r"""
          /\_/\ 
         ( -.- )
          > ^ <
        """
    else:
        return r"""
          /\_/\ 
         ( o.o )
          > ^ <
        """
