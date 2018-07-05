
def run_to_limit(limit):

    x = 1
    y = 0
    index = 1
    level = 1
    direction = "up"

    values = {(0, 0): 1}

    while True:
        value = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i, j) in values:
                    value += values[(i, j)]
        values[(x, y)] = value
        
        if value > limit:
            return value

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
            if x > level:
                direction = "up"
                level += 1

        

if __name__ == "__main__":
    INPUT = 277678
    print(run_to_limit(INPUT))
