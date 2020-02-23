#  Source.py for Algorithms Project 2
#
#  A test suite for analyzing the performance of sorting algorithms in the best,
#  most likely, and worst cases.
#
#  @author Ross Adams, Longtin Hang, and Riley Williams

# Be sure to comment your code!
import random


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


# main function
def main():
    first_list, second_list, third_list, fourth_list = generate_random_list_number(1000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))
    first_list, second_list, third_list, fourth_list = generate_random_list_number(10000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))
    first_list, second_list, third_list, fourth_list = generate_random_list_number(100000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))


if __name__ == "__main__":
    main()
