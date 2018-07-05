
import math

def manhattan_distance(address):
    level = determine_level(address)
    hour = determine_hour(address)
    
    coords = determine_coords(level, hour)
    
    return abs(coords[0]) + abs(coords[1])


def determine_coords(level, hour):
    
    if level == 0:
        return (0, 0)

    # Start conditions
    y = 1 - level
    x = level

    direction = "up"

    for index in range(hour):
        if direction == "up":
            y += 1
            if y == level:
                direction = "left"
        elif direction == "left":
            x -= 1
            if x == -level:
                direction = "down"
        elif direction == "down":
            y -= 1
            if y == -level:
                direction = "right"
        elif direction == "right":
            x += 1
            if x == level:
                direction = "boom"
        else:
            raise Exception("This shouldn't happen...")

    return (x, y)

def determine_level(address):
    return int(math.ceil(math.sqrt(address))//2)

def determine_hour(address):
    if address == 1:
        return 0

    level = determine_level(address)
    return address - ((((2*level)-1)**2)+1)

if __name__ == "__main__":
    INPUT = 277678
    print(manhattan_distance(INPUT))
