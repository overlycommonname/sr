from . import Type

standard_damages = {
    Type.strike: [6, 3, 1],
    Type.grapple: [4, 2, 1],
    Type.throw: [2, 1, 0]
}

class Attack(object):
    def __init__(self, tag, type, damage=None, weapon=0, special=''):
        self.tag = tag
        self.type = type
        if damage:
            self.damage = damage
        else:
            self.damage = standard_damages[self.type]
        self.weapon = weapon
        self.special = special

    def is_full_defense(self, defense_level):
        return defense_level >= len(self.damage)

    def resulting_damage(self, defense_level):
        if self.is_full_defense(defense_level):
            return 0
        else:
            return self.damage[defense_level]

    def print_results(self, defense_level):
        if self.is_full_defense(defense_level):
            print("Fully defended, no damage.")
        else:
            print("Damage: {}, (Special Effect: {})".format(self.resulting_damage(defense_level), self.special))