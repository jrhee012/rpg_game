class Character:

    def __init__(self):
        self.level = 0
        self.weapon = None
        self.armor = None
        self.spells = []

    def level_up(self):
        self.level += 1

    def get_info(self):
        stats = {
            'level': self.level,
            'weapon': self.weapon,
            'armor': self.armor,
            'spells': self.spells
        }

        return stats

    def update_from_last_file(self, last_file):
        print('a')


def get_str(character):
    stats = {
        'level': character.level,
        'weapon': character.weapon,
        'armor': character.armor,
        'spells': character.spells
    }

    return stats


def set_character(character):
    updated_character = Character()
    updated_character.update_from_last_file(character)

    return updated_character