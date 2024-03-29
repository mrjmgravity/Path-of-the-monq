def main(rounds):
    score1 = 0
    while True:
        for i in range(rounds):
            print(f"round:{i+1}")
            p1_input = (input("Enter symbol 1: ")).lower()
            p2_input = (input("Enter symbol 2: ")).lower()
            invalid_input_check = check_input(p1_input, p2_input)
            if invalid_input_check:
                print(invalid_input_check)
                break
            score1 += evaluate_round(p1_input, p2_input)
        else:
            break
    final_evaluation(score1)


def evaluate_round(p1, p2):
    if p1 == p2:
        return 0
    elif (p1 == "r" and p2 == "s") or (p1 == "s" and p2 == "p") or (p1 == "p" and p2 == "r"):
        return 1
    else:
        return -1


def final_evaluation(score1):
    if score1 > 0:
        print("Player 1 win!")
    elif score1 < 0:
        print("Player 2 win!")
    else:
        print("Its a Tie!")


def check_input(p1, p2):
    valid_inputs = ["r", "s", "p"]
    if p1 not in valid_inputs or p2 not in valid_inputs:
        return "Not valid input, please make sure both inputs are 'r', 's', or 'p'"
    else:
        return None


main(3)