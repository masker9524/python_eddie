def check_input(number):
    if not number.isdigit():
        print('Not a digit!')
        return False
    elif int(number) > 11 or int(number) < 0:
        print('Out of range!!')
        return False
    else:
        print('bye')
        return True


def main():
    p = False
    while not p:
        number = input('digit 1 ~ 10')
        p = check_input(number)


if __name__ == '__main__':
    main()
