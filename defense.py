import random
from .tag import Tag

random_range = [-2.6, -2.2, -1.8, -1.5, -1.2, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0, 0]

class Modifier(object):
    def __init__(self, tag_or_type, value):
        self.tag_or_type = tag_or_type
        self.value = value

generic_bonus_against_none_tag = Modifier(Tag.none, 0.5)

class Defense(object):
    def __init__(self, value=0, broken_value=0, modifiers=None, hardness=0):
        self.value = value
        self.broken_value = broken_value
        self.modifiers = modifiers or []
        self.hardness = hardness

    def run(self, attack, broken=False, should_print=False):
        weapon_penalty = max(attack.weapon - self.hardness, 0)
        modifier = sum([modifier.value for modifier in self.modifiers if modifier.tag_or_type in [attack.tag, attack.type]])
        multiplier = random.choice([-1, 1])
        randomizer = random.choice(random_range) * multiplier
        value = self.broken_value if broken else self.value
        result = max(round(value + randomizer + modifier - weapon_penalty), 0)
        if should_print:
            attack.print_results(result)
        return result
