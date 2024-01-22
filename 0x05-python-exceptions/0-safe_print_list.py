#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0

    try:
        for i in my_list:
            if i < x:
                print('{}'.format(my_list[i]), end='')
                i += 1

        print()
    except indexError:
        break
    finally:
        return i
