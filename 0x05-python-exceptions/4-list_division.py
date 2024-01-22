#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []
    div = 0
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            results.append(div)
    return (results)
