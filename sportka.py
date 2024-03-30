

def main():
    user_input()


def user_input(): #tato funkcia vypyta od pouzivatela 6 cisiel a rovno ich aj skontroluje
    numbers = []
    count = 0
    print("Welcome in guessing number game\n")

    while count < 6:
        try:
            num = int(input(f"Pick 6 number from 1 to 35: "))
            if 1 <= num <= 35:
                numbers.append(num)
                count += 1
                print(numbers)

            else:
                print("Invalid number\n")
        except ValueError:
            print("Please make sure u entered number from 1 to 35\n")

    return numbers


main()


