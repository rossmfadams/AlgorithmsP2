#  Source.py for Algorithms Project 2
#
#  A test suite for analyzing the performance of sorting algorithms in the best,
#  most likely, and worst cases.
#
#  @author Ross Adams, Longtin Hang, and Riley Williams

# Be sure to comment your code!
import bubbleSort
import selectionSort
import mergeSort
import quickSort
import arrayGenerator
from writeToFile import WriteToFile


# main function
def main():
    # instantiate write to file
    write_file = WriteToFile()

    # 100 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(100)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    # sorting 100 list with bubblesort
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print(comparisons)

    write_file.write_to_file('test', 'N^2', 'N', 10, 10, 10, 10)

    # 1000 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(1000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))
    
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print(comparisons)

    # 10000 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(10000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print(comparisons)

    write_file.close()


if __name__ == "__main__":
    main()
