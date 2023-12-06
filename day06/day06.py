

def possible_button_press_times(time, dist): 
    # print(f"Record Time: {time}, Distance: {dist}")

    possible = 0
    for i in range(time):
        speed = i 
        rest_time = time - i
        act_dist = rest_time * speed

        # print(f"Time: {rest_time}, Distance: {act_dist}")

        if act_dist > dist: 
            possible += 1
    
    print(f"Possible: {possible}")
    return possible



with open("input.txt", "r") as file:
    lines = file.readlines()

    time = lines[0].split()
    dist = lines[1].split()


    possible_mult = 1

    i = 1
    while i < len(time):
         possible_mult *= possible_button_press_times(int(time[i]), int(dist[i]))
         i += 1

    print(f"Possible Multiplied: {possible_mult}")
