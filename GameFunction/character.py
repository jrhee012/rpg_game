import json
import logging
from Items.weapons.swords import broad_sword

logger = logging.getLogger("MAIN")


class Character:
    def __init__(self):
        self.level = 0
        self.weapon = broad_sword.name
        self.armor = "none"
        self.spells = []
        self.name = "{character_name}"
        self.exp = 0
        self.total_health = 10
        self.remaining_health = 10

    def set_stats(self, stats: str = "") -> None:
        replaced_str = stats.replace('\'', '"')
        json_stats = json.loads(replaced_str)

        try:
            self.level = json_stats["level"]
            self.weapon = json_stats["weapon"]
            self.armor = json_stats["armor"]
            self.spells = json_stats["spells"]
            self.name = json_stats["name"]
            self.exp = json_stats["exp"]
            self.total_health = json_stats["total_health"]
            self.remaining_health = json_stats["remaining_health"]
        except KeyError as e:
            logger.error(e)
            logger.warn("unable to set previous character...!")

    def get_level_exp(self) -> int:
        current_level = self.level

        if current_level < 2:
            current_level = 0

        # TODO: update exp function
        exp_to_level = 75 * current_level + 100

        return exp_to_level

    def add_exp(self, exp: int = 0) -> None:
        current_exp = self.exp
        exp_needed = self.get_level_exp()

        new_exp = current_exp + exp

        if new_exp >= exp_needed:
            remaining = new_exp - exp_needed
            self.exp = remaining
            self.level_up()

            # recursively add more exp
            return self.add_exp(exp=0)
        else:
            self.exp = new_exp

        logger.debug("%s received %s exp!" % (self.name, self.exp))

    def level_up(self) -> None:
        self.level += 1
        self.remaining_health += 1
        self.total_health += 1
        self.get_level_exp()
        logger.debug("%s leveled up! level: %s" % (self.name, self.level))

    def get_info(self) -> object:
        stats = {
            "name": self.name,
            "exp": self.exp,
            "total_health": self.total_health,
            "remaining_health": self.remaining_health,
            "level": self.level,
            "weapon": self.weapon,
            "armor": self.armor,
            "spells": self.spells
        }
        return stats

    def update_from_last_file(self, last_file: str = "") -> None:
        self.set_stats(last_file)

    def attack(self, target):
        attack_pt = self.weapon


def get_info(character: json) -> object:
    stats = {
        "name": character.name,
        "exp": character.exp,
        "total_health": character.total_health,
        "remaining_health": character.remaining_health,
        "level": character.level,
        "weapon": character.weapon,
        "armor": character.armor,
        "spells": character.spells
    }
    return stats


def set_character(character: str = "") -> Character:
    updated_character = Character()
    updated_character.update_from_last_file(character)
    return updated_character
