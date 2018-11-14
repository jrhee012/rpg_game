import os
# import logging
import __root__
import datetime
from .states import State
from .character import Character, get_info, set_character
from .keys import *

root_dir = __root__.path()
logger = logging.getLogger("MAIN")


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_colour = (255, 255, 255)
        self.root_dir = root_dir
        self.save_file_dir = os.path.join(root_dir, "data", "save_files")
        self.current_save_file = None
        self.app = None

    def initialize(self, app, key_listener) -> None:
        self.app = app
        save_file_dir = self.save_file_dir
        dir_exist = os.path.isdir(save_file_dir)

        # logger.info("Houston, we have a %s", "interesting problem")

        if dir_exist is True:
            logger.info("save file directory exists!")
        else:
            os.makedirs(save_file_dir, exist_ok=True)
            logger.info("save file directory created!")

        files = os.listdir(str(save_file_dir))

        """
        check for number of save files
        only keep one save file
        """
        if len(files) > 0:
            first_file = files[0]
            character = self.set_character_from_file(first_file)
            self.delete_save_file(files[0])
        else:
            character = Character()

        logger.info("loaded character: %s" % str(character.get_info()))

        # print("app: ", app)
        # print("app name: ", app.name)
        # print(app.settings)

        new_state = State(app, key_listener)
        # new_state.update()
        app.state = new_state

        # TODO: TEST
        character.add_exp(exp=1000)

        new_state.update_character(character)
        current_file = self.create_save_file(new_state)
        self.current_save_file = current_file

        # klistr = find_key_listener()
        # logger.info("key listener: %s" % klistr)

    def set_character_from_file(self, filename: str = "") -> Character:
        file_path = self.save_file_dir + "/" + filename
        f = open(file_path, "r")
        last_character = set_character(f.readline())
        return last_character

    def create_save_file(self, new_state: State) -> str:
        filename = datetime.datetime.now().strftime("%Y%m%dT%H%M%S") + ".txt"
        save_file_location = self.save_file_dir + "/" + filename
        character = new_state.character

        logger.info("character to save: %s" % str(get_info(character)))

        f = open(str(save_file_location), "w+")
        f.write(str(get_info(character)))
        f.close()

        logger.info("save file created!")

        return save_file_location

    def delete_save_file(self, filename: str = "") -> None:
        file_location = self.save_file_dir + "/" + filename
        os.remove(file_location)
        logger.info("save file %s removed!" % filename)
