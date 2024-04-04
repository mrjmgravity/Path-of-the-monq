import random


def main():
    user_numbers = user_input()
    win_numbers = winning_number()
    evaluate(user_numbers, win_numbers)


def user_input():  # tato funkcia vypyta od pouzivatela 6 cisiel a rovno ich aj skontroluje
    numbers = []
    count = 0
    print("Welcome in guessing number game\n")

    while count < 6:
        num = int(input(f"Pick 6 number from 1 to 35: "))
        if 1 <= num <= 35:
            numbers.append(num)
            count += 1
            print(numbers)
        else:
            print("Invalid number\n")

    return numbers


def winning_number():
    win_numbers = random.sample(range(1, 36), 6)
    print(f"Toto su vyherne cisla:{win_numbers} \n")
    return win_numbers


def evaluate(random_numbers, user_numbers):
    win = set(random_numbers) & set(user_numbers)
    print("Vaše uhádnuté čísla:", win)
    print("Počet správnych čísel:", len(win))


main()
