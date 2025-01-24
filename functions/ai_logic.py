from random import  randrange

# function for AI turn
def ai_turn(sarasas):
    hor_1 = [sarasas[0], sarasas[1], sarasas[2]]
    hor_2 = [sarasas[3], sarasas[4], sarasas[5]]
    hor_3 = [sarasas[6], sarasas[7], sarasas[8]]
    vert_1 = [sarasas[0], sarasas[3], sarasas[6]]
    vert_2 = [sarasas[1], sarasas[4], sarasas[7]]
    vert_3 = [sarasas[2], sarasas[5], sarasas[8]]
    diag_1 = [sarasas[0], sarasas[4], sarasas[8]]
    diag_2 = [sarasas[2], sarasas[4], sarasas[6]]
    lines = [hor_2, vert_2, diag_1, diag_2, hor_1, hor_3, vert_1, vert_3]
    # note that for this function we prioritise the lines with center field, because they are more likely to be winning if they include a 0.
    # setting a condition to prevent running unnecessary parts of the function:
    completed = False
    # first we check if the middle field is available as it is the best choice in the game while playing 0-s:
    if sarasas[4] != "X" and sarasas[4] != "0":
        sarasas[4] = "0"
        completed = True
    # then we search for a winning line if any (needs to have two 0-s and zero X-s):
    if not completed:
        choice_0 = 0
        for lane in lines:
            lane_score = 0
            lane_x = 0
            for x in range(3):
                if lane[x] == "0":
                    lane_score += 1
                elif lane[x] == "X":
                    lane_x += 1
                else:
                    choice_0 = lane[x]
            if lane_score == 2 and lane_x == 0:
                choice_0 = "0"
                completed = True
    # if there's no winning line, check for possible player wins next turn and prevent those:
    if not completed:
        choice_0 = 0
        for lane in lines:
                lane_x = 0
                lane_score = 0
                for x in range(3):
                    if lane[x] == "0":
                        lane_score += 1
                    elif lane[x] == "X":
                        lane_x += 1
                    else:
                        choice_0 = lane[x]
                    if lane_score == 0 and lane_x == 2:
                        choice_0 = "0"
                        completed = True
    # barring the above, choose available field in a lane with one 0 and zero X-s:
    if not completed:
        choice_0 = 0
        for lane in lines:
            lane_x = 0
            lane_score = 0
            for x in range(3):
                if lane[x] == "0":
                    lane_score += 1
                elif lane[x] == "X":
                    lane_x += 1
                else:
                    choice_0 = lane[x]
                if lane_score == 1 and lane_x == 0:
                    choice_0 = "0"
                    completed = True
    # if all others are false, choose a field at random:
    if not completed:
        monkey_turn = True
        while monkey_turn:
            try:
                choice_0 = randrange(1, 9)
                if type(sarasas[choice_0 - 1]) is int and choice_0 != 0:
                    print(f"AI chose {sarasas[choice_0 - 1]}")
                    sarasas[choice_0 - 1] = "0"
                    monkey_turn = False
                    completed = True
                else:
                    continue
            except ValueError:
                continue

