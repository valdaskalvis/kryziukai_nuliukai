from functions.print import spausdinam
from functions.check import check_X, check_0, check_draw

while True:
    choice = int(input("1 - start two player game\n2 - start game against Monkey\n3 - start game vs and AI opponent\n4 - see scores\n0 - exit\n"))
    match choice:
        case 1:
            player1_name = input("Enter name for player 1 - playing with X-s:\n")
            player2_name = input("Enter name for player 2 - playing with 0-s:\n")
            sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            while True:
                spausdinam(sarasas)
                try:
                    choice_X = int(input(f"{player1_name}: choose an available field to place X: "))
                    if type(sarasas[choice_X - 1]) is int and choice_X != 0:
                        sarasas[choice_X - 1] = "X"
                        if check_X(sarasas) is True:
                            print(f"{player1_name} won!\nPlay again?")
                            break
                        if check_draw(sarasas) is True:
                            print("It's a draw!\nPlay again?")
                            break
                    else:
                        print("Invalid choice. Try again.\n")
                        continue
                    try:
                        spausdinam(sarasas)
                        choice_0 = int(input(f"{player2_name}: choose an available field to place 0: "))
                        if type(sarasas[choice_0 - 1]) is int and choice_0 != 0:
                            sarasas[choice_0 - 1] = "0"
                            if check_0(sarasas) is True:
                                print(f"{player2_name} won!\nPlay again?")
                                break
                        else:
                            print("Invalid choice. Try again.\n")
                            continue
                    except IndexError:
                        print("Invalid choice. Try again.\n")
                        continue
                except IndexError:
                    print("Invalid choice. Try again.\n")

        case 2:
            player_vs_monkey_name = input("Enter player name. You will be playing with X-s.\n")
            print("You will be playing against an opponent of a very limited intelligence. Would be a shame to lose here!")
        case 3:
            player_vs_ai_name = input("Enter player name. You will be playing with X-s.\n")
            print("You will be playing against an AI opponent, hopefully it'll be a bit of a challenge!")
        case 4:
            print("scorelist:")
        case 0:
            break




