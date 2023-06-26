# !/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    li = list()
    for i in range(list_length):
        j = 0
        try:
            j = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            j = 0
        except ZeroDivisionError:
            print("division by 0")
            j = 0
        except IndexError:
            print("out of range")
            j = 0
        finally:
            li.append(j)
    return li

