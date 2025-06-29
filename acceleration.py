import matplotlib


def acelerator_formel(velocity_goal, time):

    return ((velocity_goal / time) * time**2) * 0.5


def acelerator_sim(velocity_goal, time, detail) -> float:

    tick_growth = velocity_goal / (time * detail)

    distance = 0
    growing_velocity = 0
    velocity_record = []
    for i in range(detail * time):

        growing_velocity += tick_growth


        distance += growing_velocity / detail



    return distance



