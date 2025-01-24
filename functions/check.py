
# function for checking all possible winning lanes for player with X-s
def check_X(sarasas):
    hor_1 = [sarasas[0], sarasas[1], sarasas[2]]
    hor_2 = [sarasas[3], sarasas[4], sarasas[5]]
    hor_3 = [sarasas[6], sarasas[7], sarasas[8]]
    vert_1 = [sarasas[0], sarasas[3], sarasas[6]]
    vert_2 = [sarasas[1], sarasas[4], sarasas[7]]
    vert_3 = [sarasas[2], sarasas[5], sarasas[8]]
    diag_1 = [sarasas[0], sarasas[4], sarasas[8]]
    diag_2 = [sarasas[2], sarasas[4], sarasas[6]]
    lines = [hor_1, hor_2, hor_3, vert_1, vert_2, vert_3, diag_1, diag_2]
    for lane in lines:
        lane_score = 0
        for x in range (3):
            if lane[x] == "X":
                lane_score += 1
        if lane_score == 3:
            return True

# function for checking all possible winning lanes for player with 0-s
def check_0(sarasas):
    hor_1 = [sarasas[0], sarasas[1], sarasas[2]]
    hor_2 = [sarasas[3], sarasas[4], sarasas[5]]
    hor_3 = [sarasas[6], sarasas[7], sarasas[8]]
    vert_1 = [sarasas[0], sarasas[3], sarasas[6]]
    vert_2 = [sarasas[1], sarasas[4], sarasas[7]]
    vert_3 = [sarasas[2], sarasas[5], sarasas[8]]
    diag_1 = [sarasas[0], sarasas[4], sarasas[8]]
    diag_2 = [sarasas[2], sarasas[4], sarasas[6]]
    lines = [hor_1, hor_2, hor_3, vert_1, vert_2, vert_3, diag_1, diag_2]
    for lane in lines:
        lane_score = 0
        for x in range (3):
            if lane[x] == "0":
                lane_score += 1
        if lane_score == 3:
            return True

# function for checking for draw
def check_draw(sarasas):
    filled_values = 0
    for x in range (9):
        if sarasas[x] == "0" or sarasas[x] == "X":
            filled_values += 1
    if filled_values == 9:
        return True