def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    return [(f"Hello, my name is {name}.") for name in names ]

def assign_rooms(names):
    rooms = range(1,9)
    return [f"Hello, {names[room - 1]}! You\'ll be assigned to room {room}!" for room in rooms]

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for rooms in assign_rooms(names):
        print(rooms)
