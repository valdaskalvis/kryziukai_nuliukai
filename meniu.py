while True:
    choice = int(input("1 - start two player game\n2 - start game against Monkey\n3 - start game vs and AI opponent\n4 - see scores\n0 - exit\n"))
    match choice:
        case 1:
            player1_name = input("Enter name for player 1 - playing with X-s:\n")
            player2_name = input("Enter name for player 2 - playing with 0-s:\n")
        case 2:
            player_vs_monkey_name = input("Enter player name. You will be playing with X-s.\n")
            print("You will be playing against an opponent of a very limited intelligence. Would be a shame to lose here!")
        case 3:
            player_vs_ai_name = input("Enter player name. You will be playing with X-s.\n")
            print("You will be playing against an AI opponent, hopefully it'll be a bit of a challenge!")
        case 4:
            print("scorelist")
        case 0:
            break