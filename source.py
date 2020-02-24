#  Source.py for Algorithms Project 2
#
#  A test suite for analyzing the performance of sorting algorithms in the best,
#  most likely, and worst cases.
#
#  @author Ross Adams, Longtin Hang, and Riley Williams

# Be sure to comment your code!
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


# O(n^2) Sorting Algorithm
# Bubble Sort which will take the list and sort it by switching the numbers when they are greater than the previous number and continue doing this until the list is sorted
# Bubble Sort Algorithm used: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
def bubble_sort(arr):
    comparisons = 0
    # Swaps the 2 elements of the array
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                comparisons += 1
                swap(i - 1, i)
                swapped = True
                    
    return arr, comparisons

# main function
def main():
    first_list, second_list, third_list, fourth_list = generate_random_list_number(1000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    first_list, bubble_sort_compare_1000 = bubble_sort(first_list)
    print (bubble_sort_compare_1000)

    first_list, second_list, third_list, fourth_list = generate_random_list_number(10000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))
    
    first_list, bubble_sort_compare_10000 = bubble_sort(first_list)
    print (bubble_sort_compare_10000)

    first_list, second_list, third_list, fourth_list = generate_random_list_number(100000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    first_list, bubble_sort_compare_100000 = bubble_sort(first_list)
    print (bubble_sort_compare_100000)

if __name__ == "__main__":
    main()
