
def blow_up_directions(directions, length):
    while len(directions) < length:
        directions += directions

    return directions

def navigate_from_to_rec(start, end, directions, steps):
    index =  steps % len(directions)
    print(f"{steps} % {len(directions)} = Index {index} - {directions[index]}")
    steps += 1

    if start != end :
        if directions[index] == "L":
            start = data[start][0]
        else:
            start = data[start][1]

        navigate_from_to(start, end, directions, steps)


def navigate_from_to(start, end, directions):
    steps = 0
    for direction in directions: 
        if directions[steps] == "L":
            start = data[start][0]
        else:
            start = data[start][1]
        
        steps += 1
        if start == end:
            print(f"Steps: {steps}")
            return steps


data = {}

with open('input.txt', 'r') as file:
    directions = file.readline().rstrip("\n")
    next(file)

    for line in file: 
        key, value = line.rstrip("\n").split(' = ')
        data[key] = value.replace("(","").replace(")","").split(', ')

# print(data)

blown_directions = blow_up_directions(directions, 100000)
print(f"directions has {len(directions)} entrys")
print(f"blown directions has {len(blown_directions)} entrys")

navigate_from_to("AAA","ZZZ", blown_directions)


# navigate_from_to_rec("AAA","ZZZ", directions, 0)