import random


def main():
    mysteriousnumber = random.randint(1, 10)
    name = input("plz enter your name")
    print(f'hello, {name}, I guess you are smart enough to know the answer.')
    count = 0
    while True:
        count += 1
        if count == 5:
            print("You've reached the limit")
            print("mother fucker stupid")
            break
        number = int(input("Guess my fav number!"))
        if number == mysteriousnumber:
            print("You won. congraduation!")
            break
        elif number > mysteriousnumber:
            print("too big")
        elif number < mysteriousnumber:
            print("too small")


    # else:
    #     while (number < mysteriousnumber) or (number > mysteriousnumber):
    #         k += 1
    #         if k == 5:
    #             print("You've reached the limit")
    #             break
    #         else:
    #             if number > mysteriousnumber:
    #                 print("too big")
    #                 numberin = input("try one more time")
    #                 number = int(numberin)
    #             elif number < mysteriousnumber:
    #                 print("too small")
    #                 numberin = input("try one more time")
    #                 number = int(numberin)
    #     if k == 5:
    #         print("mother fucker stupid")
    #     else:
    #         print("You won. congraduation!")


if __name__ == '__main__':
    main()
