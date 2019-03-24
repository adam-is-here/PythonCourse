

def run():
    try:
        print('Hello and welcome our journey')
        trick = input('Please let me show you some magic trick, in order to proceed please insert a 3 digit number: ')
        print('The third digit is '+trick[2]+' Tadadam!')
    except ValueError as e:
        print('Wow, there was an error: ' + str(e))
    finally:
        print('NO matter what, this print will be PRINTED!')
    print('My program is still running')


def run_no_try():
        print('Hello and welcome our journey')
        trick = input('Please let me show you some magic trick, in order to proceed please insert a 3 digit number: ')
        print('The third digit is '+trick[2]+' Tadadam!')
        print('My program is still running')


def double_except_run():
    try:
        print('Hello and welcome our journey')
        trick = input('Please let me show you some magic trick, in order to proceed please insert a 3 digit number: ')
        print('The third digit is '+trick[2]+' Tadadam!')
    except LookupError as e:
        print('Wow, there was an error: ' + str(e))
    except:
        print('Wow, there was an unexpected error')
    print('My program is still running')


if __name__ == '__main__':

    run()
