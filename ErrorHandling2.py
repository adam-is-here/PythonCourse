def run():
    print('Hello and welcome to my wonderful program')
    id_number = input('Please provide your ID number WUTHOUT last digit: ')
    total = 0
    count = 0
    while len(id_number) != 8:
        id_number = input('You did not provided correct number, please re-enter it')
    for num in id_number:
        if count % 2 == 0:
            total += int(num) * 1
        else:
            if int(num) * 2 >= 10:
                mult = int(num) * 2
                temp = 0
                for n in str(mult):
                    temp += int(n)
                total += temp
            else:
                total += int(num) * 2
        count += 1
    last_digit = 10 - (total % 10)
    print('Your last digit is: ' + str(last_digit))

def run_wth_try():
    print('Hello and welcome to my wonderful program')
    id_number = input('Please provide your ID number WUTHOUT last digit: ')
    total = 0
    count = 0
    while len(id_number) != 8:
        id_number = input('You did not provided correct number, please re-enter it')
    try:
        for num in id_number:
            if count % 2 == 0:
                total += int(num) * 1
            else:
                if int(num) * 2 >= 10:
                    mult = int(num) * 2
                    temp = 0
                    for n in str(mult):
                        temp += int(n)
                    total += temp
                else:
                    total += int(num) * 2
            count += 1
        last_digit = 10 - (total % 10)
        print('Your last digit is: ' + str(last_digit))
    except ValueError as val:
            print('Some problems with one of the digits entered: ' + str(val))


if __name__ == '__main__':
    run_wth_try()
