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
import time
from writeToFile import WriteToFile


# main function
def main():
    from mergeSort import count
    from quickSort import q_count

    # instantiate write to file
    write_file = WriteToFile()

    # 100 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(100)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    # sorting 100 list with bubblesort
    start_time = time.perf_counter()
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print("Bubble Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Bubble Sort comparisions: ", comparisons)

    # sorting 100 list with selectionsort
    start_time = time.perf_counter()
    second_list, comparisons = selectionSort.selection_sort(second_list)
    print("Selection Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Selection Sort comparisions: ", comparisons)
    
    # sorting 100 list with mergesort
    start_time = time.perf_counter()
    third_list = mergeSort.merge_sort(third_list)
    print("Merge Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Merge Sort comparisions: ", count)

    # sorting 100 list with quicksort
    start_time = time.perf_counter()
    fourth_list = quickSort.quick_sort(fourth_list)
    print("Quick Sort time: %s seconds " % (time.perf_counter() - start_time))
    print("Quick Sort comparisions: ", q_count)

    write_file.write_to_file('test', 'N^2', 'N', 10, 10, 10, 10)
    write_file.write_to_file('test2', 'N^2', 'N', 10, 10, 10, 10)

    # 1000 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(1000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))
    
    # sorting 1000 list with bubblesort
    start_time = time.perf_counter()
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print("Bubble Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Bubble Sort comparisions: ", comparisons)

    # sorting 1000 list with selectionsort
    start_time = time.perf_counter()
    second_list, comparisons = selectionSort.selection_sort(second_list)
    print("Selection Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Selection Sort comparisions: ", comparisons)
    
    # sorting 1000 list with mergesort
    start_time = time.perf_counter()
    third_list = mergeSort.merge_sort(third_list)
    print("Merge Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Merge Sort comparisions: ", count)

    # sorting 1000 list with quicksort
    start_time = time.perf_counter()
    fourth_list = quickSort.quick_sort(fourth_list)
    print("Quick Sort time: %s seconds " % (time.perf_counter() - start_time))
    print("Quick Sort comparisions: ", q_count)

    # 10000 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(10000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    # sorting 10000 list with bubblesort
    start_time = time.perf_counter()
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    print("Bubble Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Bubble Sort comparisions: ", comparisons)

    # sorting 10000 list with selectionsort
    start_time = time.perf_counter()
    second_list, comparisons = selectionSort.selection_sort(second_list)
    print("Selection Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Selection Sort comparisions: ", comparisons)
    
    # sorting 10000 list with mergesort
    start_time = time.perf_counter()
    third_list = mergeSort.merge_sort(third_list)
    print("Merge Sort time: %s seconds" % (time.perf_counter() - start_time))
    print("Merge Sort comparisions: ", count)

    # sorting 10000 list with quicksort
    start_time = time.perf_counter()
    fourth_list = quickSort.quick_sort(fourth_list)
    print("Quick Sort time: %s seconds " % (time.perf_counter() - start_time))
    print("Quick Sort comparisions: ", q_count)

    write_file.close()


if __name__ == "__main__":
    main()
