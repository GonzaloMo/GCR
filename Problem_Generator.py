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

        self.Possible_Locations = ['SW', 'W','NW', 'N', 'S', 'SE', 'E', 'NE']
        self.Location_2_norm_coordinate = {}
        k = 0
        for x in [0, 0.5, 1]:
            for y in [0, 0.5, 1]:
                if not(x==0.5 and y==0.5):
                    self.Location_2_norm_coordinate[self.Possible_Locations[k]] = np.array([x,y])
                    k += 1

    def generate_1_room(self, Room_name, setup):
        self.number_of_rooms += 1
        self.Room_names.append(Room_name)
        self.Room_name2index[Room_name] = self.number_of_rooms-1
        self.Rooms.append(env_util.Room(Room_name, self.Room_setup[setup]))
    
    def generate_1_connection(self, Room_1, Room_2, Location):
        Bat_C = 0
        if Location == 'Random':
            loc_1 = random.choice(self.Possible_Locations)
        else:
            loc_1 = Location

        ind_1 = self.Possible_Locations.index(loc_1)
        ind_2 = int(7-ind_1)
        loc_2 = self.Possible_Locations[ind_2]
        print(Room_1)
        print(Room_2)
        id_room_1 = self.Room_name2index[Room_1]
        id_room_2 = self.Room_name2index[Room_2]  
        var = np.array([self.Rooms[id_room_1].x_delta,  self.Rooms[id_room_1].y_delta])

        coord_1 = self.Location_2_norm_coordinate[loc_1] * var
        coord_2 = self.Location_2_norm_coordinate[loc_2] * var
        self.Rooms[id_room_1].connect(Room_2, coord_1, loc_1, Bat_C)
        self.Rooms[id_room_2].connect(Room_1, coord_2, loc_2, Bat_C)

    def clear(self):
        self.Room_names = []
        self.Rooms = []

    def From_text_file(self):
        file_name = 'Problem'



