from idlelib.configdialog import changes

import matplotlib.pyplot as plt
import math

a = list(range(2,90))

b = 123
def vector_add(v1,v2):


    return [v1[0] + v2[0],v1[1] + v2[1]]
def main(speed,detail,gravity,angle):
    angle = math.radians(angle)  # convert degrees to radians if needed

    x = math.cos(angle)
    y = math.sin(angle)

    vector = [x * speed,y * speed]



    ball_cords = [0.0,0.001]




    y_record = []
    x_record = []
    gravity = 0
    gravity_growth = 18 # per second

    while ball_cords[1] > 0:


        gravity += gravity_growth / detail


        change = [vector[0] / detail,(vector[1] - gravity) / detail]


        ball_cords =  vector_add(ball_cords,change)

        x_record.append(ball_cords[0])
        y_record.append(ball_cords[1])

    return [x_record,y_record]



max_heights = []
even = False
for throw_angle in range(2,91):
    test = main(speed=250,detail=400,gravity=0,angle=throw_angle)

    even = not even


    max_heights.append(max(test[0]))



current_max = 0
current_index = 0
for index,height in enumerate(max_heights):

    if current_max < height:
        current_max = height
        current_index = index


plt.plot([i for i in range(2,91)],max_heights)

plt.show()

























