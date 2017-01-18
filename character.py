import random

class Stance(object):
    def __init__(self, name='default', defenses=[], attacks=[], choices=3):
        self.name = name
        self.defenses = defenses
        self.attacks = attacks
        self.choices = choices
        self.recent_choices = []

    def options(self):
        self.recent_choices = sorted(list(set(random.randrange(len(self.attacks)) for _ in self.choices)))
        for index, choice in enumerate(self.recent_choices):
            print("{}.  {}".format(index, self.attacks[choice].describe()))

    def clear_options(self):
        self.recent_choices = []

    def attack(self, choice_index):
        to_return = self.attacks[self.recent_choices[choice_index]]
        self.clear_options()
        return to_return

    def defend(self, attack, broken=False):
        return max([defense.run(attack, broken) for defense in self.defenses])


class Character(object):
    def __init__(self, name, stances=None, max_hp=30):
        self.name = name
        self.stances = stances or {}
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        if len(self.stances) == 1:
            self.current_stance = self.stances[self.stances.keys[0]]
        else:
            self.current_stance = None
        self.choice_indices = []
        self.last_attack = None

    def display_stances(self):
        return self.stances.keys

    def set_stance(self, name):
        if name in self.stances.keys:
            if self.current_stance:
                self.current_stance.clear_options()
            self.current_stance = self.stances[name]
        else:
            raise RuntimeError("No such stance")

    def options(self):
        self.current_stance.options()

    def attack(self, choice_index):
        self.current_stance.attack(choice_index)

    def defend(self, attack, broken=False):
        defense_level = self.current_stance.defend(attack, broken)
        attack.print_results(defense_level)
        self.current_hp -= attack.resulting_damage(defense_level)
        print("Current hp: {}".format(self.current_hp))

    def heal(self):
        self.current_hp = self.max_hp