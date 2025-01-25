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
    lines = [hor_1, hor_2, hor_3, vert_1, vert_2, vert_3, diag_1, diag_2]
    # note that this is an unwieldy and far from the best solution, but at this point I didn't want to rewrite everything with a dictionary array.
    # setting a condition to prevent running unnecessary parts of the function:
    completed = False
    # first we check if the center field is available as it is the best choice in the game while playing 0-s:
    if sarasas[4] != "X" and sarasas[4] != "0":
        sarasas[4] = "0"
        completed = True
    # then we answer with 0 in the corner if the starting player chooses center field as his starting one:
    if not completed:
        if sarasas.count("X") == 1:
            sarasas[0] = "0"
            completed = True
    # then we search for a winning line if any (needs to have two 0-s and zero X-s):
    if not completed:
        if hor_1.count("0") == 2 and hor_1.count("X") == 0:
            sarasas[0] = "0"
            sarasas[1] = "0"
            sarasas[2] = "0"
            completed = True
        elif hor_2.count("0") == 2 and hor_2.count("X") == 0:
            sarasas[3] = "0"
            sarasas[4] = "0"
            sarasas[5] = "0"
            completed = True
        elif hor_3.count("0") == 2 and hor_2.count("X") == 0:
            sarasas[6] = "0"
            sarasas[7] = "0"
            sarasas[8] = "0"
            completed = True
        elif vert_1.count("0") == 2 and vert_1.count("X") == 0:
            sarasas[0] = "0"
            sarasas[3] = "0"
            sarasas[6] = "0"
            completed = True
        elif vert_2.count("0") == 2 and vert_2.count("X") == 0:
            sarasas[1] = "0"
            sarasas[4] = "0"
            sarasas[7] = "0"
            completed = True
        elif vert_3.count("0") == 2 and vert_3.count("X") == 0:
            sarasas[2] = "0"
            sarasas[5] = "0"
            sarasas[8] = "0"
            completed = True
        elif diag_1.count("0") == 2 and diag_1.count("X") == 0:
            sarasas[0] = "0"
            sarasas[4] = "0"
            sarasas[8] = "0"
            completed = True
        elif diag_2.count("0") == 2 and diag_2.count("X") == 0:
            sarasas[2] = "0"
            sarasas[4] = "0"
            sarasas[6] = "0"
            completed = True
    # if there's no winning line, check for possible player wins next turn and prevent those:
    # this is where going with a list array starts hurting...
    if not completed:
        if hor_1.count("0") == 0 and hor_1.count("X") == 2:
            if isinstance(sarasas[0], int):
                sarasas[0] = "0"
            if isinstance(sarasas[1], int):
                sarasas[1] = "0"
            if isinstance(sarasas[2], int):
                sarasas[2] = "0"
            completed = True
        elif hor_2.count("0") == 0 and hor_2.count("X") == 2:
            if isinstance(sarasas[3], int):
                sarasas[3] = "0"
            if isinstance(sarasas[4], int):
                sarasas[4] = "0"
            if isinstance(sarasas[5], int):
                sarasas[5] = "0"
            completed = True
        elif hor_3.count("0") == 0 and hor_3.count("X") == 2:
            if isinstance(sarasas[6], int):
                sarasas[6] = "0"
            if isinstance(sarasas[7], int):
                sarasas[7] = "0"
            if isinstance(sarasas[8], int):
                sarasas[8] = "0"
            completed = True
        elif vert_1.count("0") == 0 and vert_1.count("X") == 2:
            if isinstance(sarasas[0], int):
                sarasas[0] = "0"
            if isinstance(sarasas[3], int):
                sarasas[3] = "0"
            if isinstance(sarasas[6], int):
                sarasas[6] = "0"
            completed = True
        elif vert_2.count("0") == 0 and vert_2.count("X") == 2:
            if isinstance(sarasas[1], int):
                sarasas[1] = "0"
            if isinstance(sarasas[4], int):
                sarasas[4] = "0"
            if isinstance(sarasas[7], int):
                sarasas[7] = "0"
            completed = True
        elif vert_3.count("0") == 0 and vert_3.count("X") == 2:
            if isinstance(sarasas[2], int):
                sarasas[2] = "0"
            if isinstance(sarasas[5], int):
                sarasas[5] = "0"
            if isinstance(sarasas[8], int):
                sarasas[8] = "0"
            completed = True
        elif diag_1.count("0") == 0 and diag_1.count("X") == 2:
            if isinstance(sarasas[0], int):
                sarasas[0] = "0"
            if isinstance(sarasas[4], int):
                sarasas[4] = "0"
            if isinstance(sarasas[8], int):
                sarasas[8] = "0"
            completed = True
        elif diag_2.count("0") == 0 and diag_2.count("X") == 2:
            if isinstance(sarasas[2], int):
                sarasas[2] = "0"
            if isinstance(sarasas[4], int):
                sarasas[4] = "0"
            if isinstance(sarasas[6], int):
                sarasas[6] = "0"
            completed = True
    # best X-s player strategy for turn 2 is placing his second x diagonally in the opposite corner from the first one.
    # to counter that, the AI must choose an appropriate non-corner field, otherwise it loses:
    if not completed:
        if sarasas[4] != "X" and sarasas.count("X") == 2 and diag_1.count("X") == 2 and diag_1.count("0") == 1:
            sarasas[7] = "0"
            completed = True
        elif sarasas[4] != "X" and sarasas.count("X") == 2 and diag_2.count("X") == 2 and diag_2.count("0") == 1:
            sarasas[5] = "0"
            completed = True
    # however, if we're on a second turn and player has 2 X-s in the same diagonal as AI's 0,
    # AI must choose a corner field
    if not completed:
        if sarasas[4] == "X" and sarasas.count("X") == 2 and diag_1.count("X") == 2 and diag_1.count("0") == 1:
            sarasas[2] = "0"
            completed = True
        elif sarasas[4] == "X" and sarasas.count("X") == 2 and diag_2.count("X") == 2 and diag_2.count("0") == 1:
            sarasas[0] = "0"
            completed = True
    # there's a random function just in case all options above do not apply ("monkey" option):
    if not completed:
        monkey_turn = True
        while monkey_turn:
            try:
                choice_0 = randrange(1, 9)
                if type(sarasas[choice_0 - 1]) is int and choice_0 != 0:
                    sarasas[choice_0 - 1] = "0"
                    monkey_turn = False
                    completed = True
                else:
                    continue
            except ValueError:
                continue
    # the only strategy the player can employ that allows to occasionally win is to start with a corner X,
    # then respond with non-adjacent edge field - in this case the "AI" will respond at random and may lose.
    # this is left here as a random win possibility because the "perfect" never losing AI is absolutely unfun.
    # alternately a proper AI response could be coded here, but a, say, 10% chance of a random turn choice at
    # any point could be introduced to leave the player a chance to win.