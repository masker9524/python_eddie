def main():
    number = input('digit 1 ~ 10')
    while not number.isdigit():
        number = input('input again!!!')
    number = int(number)
    while number > 10 or number < 1:
        number = input('input Again!!!')
        number = int(number)
    print('Bye')

if __name__ == '__main__':
    main()