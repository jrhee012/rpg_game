import datetime
import logging
from enum import Enum
from .character import Character
# from GameFunction import screen
# from .screen import Background
# from start_adventure import app

logger = logging.getLogger("__MAIN__")


class StateValue(Enum):
    INITIAL_SCREEN: str = "INITIAL_SCREEN"
    START_SCREEN: str = "START_SCREEN"
    MAIN_MENU: str = "MAIN_MENU"

    @staticmethod
    def get_next_state(current_state):
        if current_state.value == StateValue.INITIAL_SCREEN.value:
            return StateValue.START_SCREEN
        elif current_state.value == StateValue.START_SCREEN.value:
            return StateValue.MAIN_MENU
        else:
            return StateValue.INITIAL_SCREEN
        # TODO: ADD MORE ^^^


class State:
    def __init__(self, app, key_listener):
        self.id = datetime.datetime.now().isoformat()
        self.name = StateValue.INITIAL_SCREEN
        self.character = None
        self.app = app
        self.key_listener = key_listener

        logger.info("state created!")

    def character_to_string(self) -> str:
        string = str(self.character)
        return string

    def update_character(self, character: Character) -> None:
        self.character = character

    def update(self) -> None:
        next_state = StateValue.get_next_state(self.name)
        self.name = next_state
        self.app.screen.update_state(self)



# def get_state(states) -> State:
#     if len(states) < 1:
#         raise NotImplementedError
#
#     return states[0]
