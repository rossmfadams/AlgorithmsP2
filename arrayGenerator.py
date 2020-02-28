# This program returns the N amount of elements in an array
import random


# create four lists of random numbers
def generate_random_list_number(number):
    first_list = []
    second_list = []
    third_list = []
    fourth_list = []

    for i in range(number):
        value = random.randint(0, number)
        first_list.append(value)
        second_list.append(value)
        third_list.append(value)
        fourth_list.append(value)

    return first_list, second_list, third_list, fourth_list


# Take in sorted lists and randomly pick an index to swap with index 100
# return the lists
def randomizer(f, s, t, fou):
    value = random.randint(0, 1000)
    f[100], f[value] = f[value], f[100]
    s[100], s[value] = s[value], s[100]
    t[100], t[value] = t[value], t[100]
    fou[100], fou[value] = fou[value], fou[100]
    return f, s, t, fou