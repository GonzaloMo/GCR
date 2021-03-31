import numpy as np
import matplotlib.pyplot as plt

class Room(object):
    def __init__(self, room_name, type_r, mean=3, sd=1, x_lim=[0, 5], y_lim=[0, 5], eps=.1):
        self.room_name = room_name
        self.x_lim = np.asarray(x_lim)
        self.x_delta = x_lim[1] - x_lim[0]  
        self.y_lim = np.asarray(y_lim)
        self.y_delta = y_lim[1] - y_lim[0]  
        
        self.type_r = type_r
        self.connections = {'Room': [] ,'Location': [], 'Coordinates': [], 'Battery Consumption': []}
        if type_r == 'Initial':
            self.max_piece = 0
            self.charging = np.array([self.x_lim[0]+eps, self.y_lim[0]+eps]) 
            self.bin = np.array([self.x_lim[0]+eps, (self.y_lim[0] + self.y_lim[1])/2])

        elif type_r == 'Set-location-number':
            self.max_piece = 4
            self.pieces_loc = np.array([[self.x_lim[0]+eps, self.y_lim[0]+eps], [self.x_lim[0]+eps, self.y_lim[1]-eps], [self.x_lim[1]-eps, self.y_lim[0]+eps], [self.x_lim[1]-eps, self.y_lim[1]-eps]])

        elif type_r == 'Set-location':
            piece = np.random.rand(4)
            pieces = np.array([[self.x_lim[0]+eps, self.y_lim[0]+eps], [self.x_lim[0]+eps, self.y_lim[1]-eps], [self.x_lim[1]-eps, self.y_lim[0]+eps], [self.x_lim[1]-eps, self.y_lim[1]-eps]])
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
                x = self.x_delta * np.random.rand() + self.x_lim[0]
                y = self.y_delta * np.random.rand() + self.y_lim[0]
                piece.append([round(x,2), round(y,2)]) 
            self.pieces_loc = np.asarray(piece)

        else:
           raise Exception("Not a valid type of Room choose:\n Initial\n Set-location-number\n Set-location\n Normal-Distribution") 

    def connect(self,Room_name, Pos, Loc, Bat_C):
        self.connections['Room'].append(Room_name)
        self.connections['Location'].append(Loc)
        self.connections['Coordinates'].append(Pos)
        self.connections['Battery Consumption'].append(Bat_C)

    def render(self, x_var=0, y_var=0, fig=0):
        x_lim = self.x_lim + x_var
        y_lim = self.y_lim + y_var

        if fig==0:
            plt.figure(self.room_name)
        else:
            plt.figure(fig)

        # upper wall
        plt.plot(x_lim, [y_lim[1], y_lim[1]], 'k')
        # lower wall
        plt.plot(x_lim, [y_lim[0], y_lim[0]], 'k')
        # Left wall
        plt.plot([x_lim[0], x_lim[0]], y_lim, 'k')
        # Right wall
        plt.plot([x_lim[1], x_lim[1]], y_lim, 'k')

        if self.type_r == 'Initial':
            charging = self.charging + np.array([x_var, y_var])  
            trash_bin = self.bin + np.array([x_var, y_var]) 
            plt.plot(charging[0], charging[1], 'og')
            plt.plot(trash_bin[0], trash_bin[1], 'ob')
        else:
            for i in range(0, self.max_piece):
                piece = self.pieces_loc[i,:] + np.array([x_var, y_var]) 
                plt.plot(piece[0], piece[1], 'or')

        for i in self.connections['Coordinates']:
            conn_loc = i + np.array([x_var, y_var]) 
            plt.plot(conn_loc[0], conn_loc[1], '+g')

        

        




