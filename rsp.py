def main(rounds):
    score1 = 0
    for i in range(rounds):
        print(f"round:{i+1}")
        p1_input = (input("Enter symbol 1: ")).lower()
        p2_input = (input("Enter symbol 2: ")).lower()
        score1 += evaluate_round(p1_input, p2_input)
        #score1 = score1 + evaluate_round(p1_input, p2_input)
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


main(3)