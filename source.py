#  Source.py for Algorithms Project 2
#
#  A test suite for analyzing the performance of sorting algorithms in the best,
#  most likely, and worst cases.
#
#  @author Ross Adams, Longtin Hang, and Riley Williams

# Be sure to comment your code!
import random
import bubbleSort
import selectionSort
import mergeSort
import quickSort
import writeToFile

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


# main function
def main():

    first_list, second_list, third_list, fourth_list = generate_random_list_number(100)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print(comparisons)

    first_list, second_list, third_list, fourth_list = generate_random_list_number(1000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))
    
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print(comparisons)

    first_list, second_list, third_list, fourth_list = generate_random_list_number(10000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print(comparisons)

if __name__ == "__main__":
    main()
