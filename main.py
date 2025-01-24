from functions.print import spausdinam
from functions.check import check_X, check_0, check_draw
from random import randrange
from functions.ai_logic import ai_turn
from time import sleep

while True:
    choice = int(input("1 - start two player game\n2 - start game against Monkey\n3 - start game vs and AI opponent\n0 - exit\n"))
    match choice:
        case 1:
            game_on = True
            player1_name = input("Enter name for player 1 - playing with X-s: ")
            player2_name = input("Enter name for player 2 - playing with 0-s: ")
            # creating the list array for available fields with numbers to make choosing them easier
            sarasas: list[int | str]  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # "game_on" switch to handle the issue of the loop still running when player2 wins
            while game_on:
                spausdinam(sarasas)
                try:
                    # player1 turn: choose an available field, upon correct choice - update the field and check for end of game scenarios
                    choice_X = int(input(f"{player1_name}: choose an available field to place X: "))
                    if type(sarasas[choice_X - 1]) is int and choice_X != 0:
                        sarasas[choice_X - 1] = "X"
                        if check_X(sarasas) is True:
                            spausdinam(sarasas)
                            print(f"{player1_name} won!\nPlay again?\n")
                            break
                        if check_draw(sarasas) is True:
                            spausdinam(sarasas)
                            print("It's a draw!\nPlay again?\n")
                            break
                    else:
                        print("Invalid choice. Try again.")
                        continue
                    # Below is the player 2 part with a "player2_turn" switch for a successful turn
                    player2_turn = True
                    while player2_turn:
                        try:
                            spausdinam(sarasas)
                            # player2 turn: choose an available field, upon correct choice - update the field and check for end of game scenarios
                            choice_0 = int(input(f"{player2_name}: choose an available field to place 0: "))
                            if type(sarasas[choice_0 - 1]) is int and choice_0 != 0:
                                sarasas[choice_0 - 1] = "0"
                                player2_turn = False
                                if check_0(sarasas) is True:
                                    spausdinam(sarasas)
                                    print(f"{player2_name} won!\nPlay again?\n")
                                    game_on = False
                            else:
                                print("Invalid choice. Try again.")
                                continue
                        except (IndexError,ValueError):
                            print("Invalid choice. Try again.")
                            continue
                except (IndexError,ValueError):
                    print("Invalid choice. Try again.")

        case 2:
            monkey_game_on = True
            print("You will be playing with X-s.")
            print("You will be playing against an opponent of a very limited intelligence. Would be a shame to lose here!")
            sarasas: list[int | str] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            while monkey_game_on:
                spausdinam(sarasas)
                try:
                    # player turn: choose an available field, upon correct choice - update the field and check for end of game scenarios
                    choice_X = int(input(f"Please choose an available field to place X: "))
                    if type(sarasas[choice_X - 1]) is int and choice_X != 0:
                        sarasas[choice_X - 1] = "X"
                        if check_X(sarasas) is True:
                            spausdinam(sarasas)
                            print(f"You won!\nPlay again?\n")
                            break
                        if check_draw(sarasas) is True:
                            spausdinam(sarasas)
                            print("It's a draw!\nPlay again?\n")
                            break
                    else:
                        print("Invalid choice. Try again.")
                        continue
                    spausdinam(sarasas)
                    print("Monkey smashes the keyboard!")
                    # monkey takes some time:
                    sleep(2)
                    # monkey turn: choose an available field at random, update the field and check for end of game scenarios
                    monkey_turn = True
                    while monkey_turn:
                        try:
                            choice_0 = randrange(1, 9)
                            if type(sarasas[choice_0 - 1]) is int and choice_0 != 0:
                                print(f"Monkey hits {sarasas[choice_0 - 1]}")
                                sarasas[choice_0 - 1] = "0"
                                monkey_turn = False
                                if check_0(sarasas) is True:
                                    spausdinam(sarasas)
                                    print(f"Monkey won - shame on you!\nPlay again?\n")
                                    monkey_game_on = False
                            else:
                                continue
                        except ValueError:
                            continue
                except (IndexError,ValueError):
                    print("Invalid choice. Try again.")

        # to be implemented
        case 3:
            print("You will be playing with X-s.")
            print("You will be playing against an AI opponent, hopefully it'll be a bit of a challenge!")
            ai_game_on = True
            sarasas: list[int | str] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            while ai_game_on:
                spausdinam(sarasas)
                try:
                    # player turn: choose an available field, upon correct choice - update the field and check for end of game scenarios
                    choice_X = int(input(f"Please choose an available field to place X: "))
                    if type(sarasas[choice_X - 1]) is int and choice_X != 0:
                        sarasas[choice_X - 1] = "X"
                        if check_X(sarasas) is True:
                            spausdinam(sarasas)
                            print(f"You won!\nPlay again?\n")
                            break
                        if check_draw(sarasas) is True:
                            spausdinam(sarasas)
                            print("It's a draw!\nPlay again?\n")
                            break
                    else:
                        print("Invalid choice. Try again.")
                        continue
                    spausdinam(sarasas)
                    print("AI turn.")
                    # AI turn: choose an available field, update the field and check for end of game scenarios
                    ai_turn(sarasas)
                    if check_0(sarasas) is True:
                        spausdinam(sarasas)
                        print(f"AI won!\nPlay again?\n")
                        ai_game_on = False
                except (IndexError, ValueError):
                    print("Invalid choice. Try again.")

        case 0:
            print("Game over.")
            break




