
def blow_up_directions(directions, length):
    while len(directions) < length:
        directions += directions

    return directions

def navigate_from_to(start, end, directions):
    steps = 0
    for direction in directions: 
        if directions[steps] == "L":
            start = data[start][0]
        else:
            start = data[start][1]
        
        steps += 1
        if start == end:
            return steps

def get_nodes_by_last_char(nodes,last):
    starting_nodes = []
    for node in nodes:
        if node.endswith(last):
            starting_nodes.append(node)
    
    return starting_nodes

def single_path(nodes,directions):
    nodes_data = {}
    nodes_steps =[]
    for node in nodes:         
        steps = 0
        start = node
        z_stops = {}
        
        # print(f"Calculate for Node {node}")
        for direction in directions: 
            if directions[steps] == "L":
                start = data[start][0]
            else:
                start = data[start][1]
            
            steps += 1
            # print(start)
            if start.endswith("Z"):
                # print(start)
                z_stops[start] = steps

            if start in nodes or start in z_stops:
                # print(f"Steps: {steps}")
                nodes_data[node] = steps, start
                nodes_steps.append(steps)
                break
    
    # print(nodes_data)
    return nodes_steps

data = {}

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_array(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result


with open('input.txt', 'r') as file:
    directions = file.readline().rstrip("\n")
    next(file)

    for line in file: 
        key, value = line.rstrip("\n").split(' = ')
        data[key] = value.replace("(","").replace(")","").split(', ')

blown_directions = blow_up_directions(directions, 10000000)
print(f"directions has {len(directions)} entrys")
print(f"blown directions has {len(blown_directions)} entrys")

steps = navigate_from_to("AAA","ZZZ", blown_directions)
print(f"Steps from AAAA to ZZZ: {steps}")

starting_nodes = get_nodes_by_last_char(data,"A")
print(f"{len(starting_nodes)} Starting nodes detected: {starting_nodes}")

starting_nodes_steps = single_path(starting_nodes,blown_directions)

print(f"Shortest way from start to recursion: {starting_nodes_steps}")
print(f"Least common multiple of all shortest ways: {lcm_array(starting_nodes_steps)}")
