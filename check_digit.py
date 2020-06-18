def main():
    number = input('digit 1 ~ 10')
    p = True
    while p:
        if not number.isdigit():
            number = input('input again!!!')
        elif int(number) > 11 or int(number) < 0:
            number = input('input Again!!!')
        else:
            print('bye')
            p = False


if __name__ == '__main__':
    main()
