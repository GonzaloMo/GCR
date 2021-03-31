# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 12:52:08 2021

@author: monte
"""

import Env_utils as env_util
import numpy as np
import random
import Problem_Generator

PG = Problem_Generator.GCR_PG()
number_of_rooms = 4
for i in range(0,number_of_rooms):
    PG.generate_1_room('Room_'+str(i),random.randint(0, 3))

PG.generate_1_connection(PG.Room_names[0],PG.Room_names[1],'Random')
Rooms = PG.Rooms
# Render
for i in range(0,number_of_rooms):
    Rooms[i].render()

"""

for i in range(0,4):
    k = 0
    if i ==1:
        Room = Room_1
    elif i ==2:
        Room = Room_2
    elif i ==3:
        Room = Room_3
    elif i ==4:
        Room = Room_4
    for j in Room_names:
        k += 1
        if  Room.connections['Room']
            line_connection[i,k] =  Room.connections['Location']
fig = 'Scheme'
Room_1.render(x_var=0, y_var=0, fig=fig)
Room_2.render(x_var=10, y_var=0, fig=fig)
Room_3.render(x_var=10, y_var=10, fig=fig)
Room_4.render(x_var=0, y_var=10, fig=fig)
"""