import Env_utils as env_util
import numpy as np
import random

class GCR_PG(object):
    def __init__(self):
        self.Room_setup = ['Initial', 'Set-location-number','Set-location','Normal-Distribution']
        self.Room_names = []
        self.Room_name2index = {}
        self.Rooms = []
        self.number_of_rooms = 0

    def generate_1_room(self, Room_name, setup):
        self.number_of_rooms += 1
        self.Room_names.append(Room_name)
        self.Room_name2index[Room_name] = self.number_of_rooms-1
        self.Rooms.append(env_util.Room(Room_name, self.number_of_rooms-1, self.Room_setup[setup]))
    
    def generate_1_connection(self, Room_1, Room_2, loc_1, loc_2,Bat_C):
        self.Rooms[Room_1].connect(Room_2, loc_1, Bat_C)
        self.Rooms[Room_2].connect(Room_1, loc_2, Bat_C)

    def clear(self):
        self.Room_names = []
        self.Rooms = []

    def From_text_file(self):
        file_name = 'Problem'



