import datetime


class State:

    def __init__(self):
        self.start_time = datetime.datetime.now().isoformat()
        self.end_time = None
        self.character = None

    def to_string(self):
        string = str(self.character)
        print('ssss')
        print(string)
        return string

    def update_character(self, character):
        self.character = character
