import os
import sys
import __root__
import datetime
from .states import State
from .character import Character, get_str, set_character

root_dir = __root__.path()


class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_colour = (255, 255, 255)
        self.root_dir = root_dir
        self.save_file_dir = os.path.join(root_dir, 'data', 'save_files')
        self.current_save_file = None

    def initialize(self):
        # root_dir = __root__.path()
        # print(datetime.datetime.now().isoformat())
        # print(datetime.datetime.now().strftime("%Y%m%dT%H%M%S"))
        # print(root_dir)

        save_file_dir = os.path.join(root_dir, 'data', 'save_files')
        # print(save_file_dir)

        dir_exist = os.path.isdir(save_file_dir)
        if dir_exist is True:
            print('save file directory exists!')
        else:
            os.makedirs(save_file_dir, exist_ok=True)
            print('save file directory created!')

        files = os.listdir(str(save_file_dir))
        # print('files:', files)

        if len(files) > 24:
            self.delete_save_file(files)

        first_file = '20181112T234015.txt'
        print('frist: ', first_file)
        self.set_character_from_file(first_file)

        new_state = State()
        new_character = Character()
        print(get_str(new_character))
        new_state.update_character(new_character)
        current_file = self.create_save_file(new_state)
        self.current_save_file = current_file


        # if len(files) < 1:

    def set_character_from_file(self, file):
        file_path = self.save_file_dir + '/' + file
        print(file_path)
        f = open(file_path, 'r')

        print('ssssssdeeer222', f.readline())

    def create_save_file(self, new_state):
        filename = datetime.datetime.now().strftime("%Y%m%dT%H%M%S") + '.txt'
        print(filename)
        save_file_location = self.save_file_dir + '/' + filename
        print(save_file_location)
        # print(new_state.to_string())
        character = new_state.character
        f = open(str(save_file_location), 'w+')
        f.write(str(get_str(character)))
        f.close()
        print('save file created!')

        return save_file_location

    def delete_save_file(self, files=[]):
        last_file = files[(len(files) - 1)]
        file_location = self.save_file_dir + '/' + last_file
        os.remove(file_location)
        print('%s removed!' % last_file)