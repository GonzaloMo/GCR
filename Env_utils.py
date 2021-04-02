import numpy as np
import matplotlib.pyplot as plt

class Room(object):
    def __init__(self, room_name, room_id, type_r, mean=3, sd=1, x_lim=[0, 5], y_lim=[0, 5], eps=.1, margin_t=0.5):
        self.room_name = room_name
        self.room_id = room_id
        self.x_lim = np.asarray(x_lim)
        self.x_delta = x_lim[1] - x_lim[0]  
        self.y_lim = np.asarray(y_lim)
        self.y_delta = y_lim[1] - y_lim[0]  
        
        self.type_r = type_r
        self.Possible_Locations = ['SW', 'W','NW', 'N', 'S', 'SE', 'E', 'NE']
        self.Location_2_norm_coordinate = {}

        k = 0
        for x in [0, 0.5, 1]:
            for y in [0, 0.5, 1]:
                if not(x==0.5 and y==0.5):
                    self.Location_2_norm_coordinate[self.Possible_Locations[k]] = np.array([x,y])
                    k += 1
        
        self.connections = {'id': [], 'Location': [],  'Battery Consumption': []}
        if type_r == 'Initial':
            self.max_piece = 0
            self.charging = np.array([self.x_delta/6, self.y_lim[0]]) 
            self.bin = np.array([self.x_lim[0], 6*self.y_delta/10])

        elif type_r == 'Set-location-number':
            self.max_piece = 4
            self.pieces_loc = np.array([[self.x_lim[0]+margin_t, self.y_lim[0]+margin_t], [self.x_lim[0]+margin_t, self.y_lim[1]-margin_t], [self.x_lim[1]-margin_t, self.y_lim[0]+margin_t], [self.x_lim[1]-margin_t, self.y_lim[1]-margin_t]])

        elif type_r == 'Set-location':
            piece = np.random.rand(4)
            pieces = np.array([[self.x_lim[0]+margin_t, self.y_lim[0]+margin_t], [self.x_lim[0]+margin_t, self.y_lim[1]-margin_t], [self.x_lim[1]-margin_t, self.y_lim[0]+margin_t], [self.x_lim[1]-margin_t, self.y_lim[1]-margin_t]])
            pieces_loc = []
            self.max_piece = 0
            for i in range(0,4):
                if piece[i] > 0.5:
                    pieces_loc.append(pieces[i,:]) 
                    self.max_piece += 1
            self.pieces_loc = np.asarray(pieces_loc)

        elif type_r == 'Normal-Distribution':
            self.max_piece =int( sd*np.random.normal() + mean)
            piece = []
            for i in range(0,self.max_piece):
                x = (self.x_delta-2*margin_t) * np.random.rand() + self.x_lim[0]+margin_t
                y = (self.y_delta-2*margin_t) * np.random.rand() + self.y_lim[0]+margin_t
                piece.append([round(x,2), round(y,2)]) 
            self.pieces_loc = np.asarray(piece)

        else:
           raise Exception("Not a valid type of Room choose:\n Initial\n Set-location-number\n Set-location\n Normal-Distribution") 

    def connect(self, r_id, Loc, Bat_C):
        self.connections['id'].append(r_id)
        self.connections['Location'].append(Loc)
        self.connections['Battery Consumption'].append(Bat_C)
