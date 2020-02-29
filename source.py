#  Source.py for Algorithms Project 2
#
#  A test suite for analyzing the performance of sorting algorithms in the best,
#  most likely, and worst cases.
#
#  @author Ross Adams, Longtin Hang, and Riley Williams

# Be sure to comment your code!
import bubbleSort
import selectionSort
from mergeSort import MergeSort
import quickSort
import arrayGenerator
import time
from writeToFile import WriteToFile
import sys


# main function
def main():
    from quickSort import q_count

    sys.setrecursionlimit(5000)

    # instantiate write to file
    write_file = WriteToFile()
    merge_sort = MergeSort()

    # 100 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(100)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    # sorting 100 list with bubblesort
    start_time = time.perf_counter()
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    end_time = time.perf_counter()
    print("Bubble Sort time: %s seconds" % (end_time - start_time))
    print("Bubble Sort comparisions: ", comparisons)

    # Creating the semisorted list
    first_list = arrayGenerator.randomizer(first_list)

    # sorting 100 semisorted list with bubblesort
    start_time_semisorted = time.perf_counter()
    first_list, semisorted_comparisons = bubbleSort.bubble_sort(first_list)
    end_time_semisorted = time.perf_counter()
    print("Bubble Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    print("Bubble Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Bubble Sort data to the file
    write_file.write_to_file('Bubble Sort', 'O(n^2)', 'O(n)', 100, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)

    # sorting 100 list with selectionsort
    start_time = time.perf_counter()
    second_list, comparisons = selectionSort.selection_sort(second_list)
    end_time = time.perf_counter()
    print("Selection Sort time: %s seconds" % (end_time - start_time))
    print("Selection Sort comparisions: ", comparisons)

    # Creating the semisorted list
    second_list = arrayGenerator.randomizer(second_list)

    # sorting 100 semisorted list with selectionsort
    start_time_semisorted = time.perf_counter()
    second_list, semisorted_comparisons = selectionSort.selection_sort(first_list)
    end_time_semisorted = time.perf_counter()
    print("Selection Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    print("Selection Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Selection Sort data to the file
    write_file.write_to_file('Selection Sort', 'O(n^2)', 'O(n^2)', 100, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)
    
    # sorting 100 list with mergesort
    start_time = time.perf_counter()
    third_list = merge_sort.merge_sort(third_list)
    end_time = time.perf_counter()
    print("Merge Sort time: %s seconds" % (end_time - start_time))
    comparisons = merge_sort.count
    print("Merge Sort comparisions: ", merge_sort.count)

    # Creating the semisorted list
    third_list = arrayGenerator.randomizer(third_list)

    # sorting 100 semisorted list with mergesort
    start_time_semisorted = time.perf_counter()
    third_list = merge_sort.merge_sort(third_list)
    end_time_semisorted = time.perf_counter()
    print("Merge Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    semisorted_comparisons = merge_sort.count
    print("Merge Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Merge Sort data to the file
    write_file.write_to_file('Merge Sort', 'O(nlog(n))', 'O(nlog(n))', 100, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)
   
    # sorting 100 list with quicksort
    start_time = time.perf_counter()
    quickSort.quick_sort(fourth_list)
    end_time = time.perf_counter()
    print("Quick Sort time: %s seconds " % (end_time - start_time))
    comparisons = quickSort.q_count
    print("Quick Sort comparisions: ", quickSort.q_count)


    # Creating the semisorted list
    fourth_list = arrayGenerator.randomizer(fourth_list)

    # sorting 100 semisorted list with quicksort
    start_time_semisorted = time.perf_counter()
    quickSort.quick_sort(fourth_list)
    end_time_semisorted = time.perf_counter()
    print("Quick Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    semisorted_comparisons = quickSort.q_count
    print("Quick Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Quick Sort data to the file
    write_file.write_to_file('Quick Sort', 'O(n^2)', 'O(nlog(n))', 100, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)


    # 1000 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(1000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))
    
    # sorting 1000 list with bubblesort
    start_time = time.perf_counter()
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    end_time = time.perf_counter()
    print("Bubble Sort time: %s seconds" % (end_time - start_time))
    print("Bubble Sort comparisions: ", comparisons)

    # Creating the semisorted list
    first_list = arrayGenerator.randomizer(first_list)

    # sorting 1000 semisorted list with bubblesort
    start_time_semisorted = time.perf_counter()
    first_list, semisorted_comparisons = bubbleSort.bubble_sort(first_list)
    end_time_semisorted = time.perf_counter()
    print("Bubble Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    print("Bubble Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Bubble Sort data to the file
    write_file.write_to_file('Bubble Sort', 'O(n^2)', 'O(n)', 1000, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)

    # sorting 1000 list with selectionsort
    start_time = time.perf_counter()
    second_list, comparisons = selectionSort.selection_sort(second_list)
    end_time = time.perf_counter()
    print("Selection Sort time: %s seconds" % (end_time - start_time))
    print("Selection Sort comparisions: ", comparisons)

    # Creating the semisorted list
    second_list = arrayGenerator.randomizer(second_list)

    # sorting 1000 semisorted list with selectionsort
    start_time_semisorted = time.perf_counter()
    second_list, semisorted_comparisons = selectionSort.selection_sort(first_list)
    end_time_semisorted = time.perf_counter()
    print("Selection Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    print("Selection Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Selection Sort data to the file
    write_file.write_to_file('Selection Sort', 'O(n^2)', 'O(n^2)', 1000, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)
    
    # sorting 1000 list with mergesort
    start_time = time.perf_counter()
    third_list = merge_sort.merge_sort(third_list)
    end_time = time.perf_counter()
    print("Merge Sort time: %s seconds" % (end_time - start_time))
    print("Merge Sort comparisions: ", merge_sort.count)

    # Creating the semisorted list
    third_list = arrayGenerator.randomizer(third_list)

    # sorting 1000 semisorted list with mergesort
    start_time_semisorted = time.perf_counter()
    third_list = merge_sort.merge_sort(third_list)
    end_time_semisorted = time.perf_counter()
    print("Merge Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    semisorted_comparisons = merge_sort.count
    print("Merge Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Merge Sort data to the file
    write_file.write_to_file('Merge Sort', 'O(nlog(n))', 'O(nlog(n))', 1000, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)

    # sorting 1000 list with quicksort
    start_time = time.perf_counter()
    quickSort.quick_sort(fourth_list)
    end_time = time.perf_counter()
    print("Quick Sort time: %s seconds " % (end_time - start_time))
    comparisons = quickSort.q_count
    print("Quick Sort comparisions: ", quickSort.q_count)

    # Creating the semisorted list
    fourth_list = arrayGenerator.randomizer(fourth_list)

    # sorting 1000 semisorted list with quicksort
    start_time_semisorted = time.perf_counter()
    quickSort.quick_sort(fourth_list)
    end_time_semisorted = time.perf_counter()
    print("Quick Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    semisorted_comparisons = quickSort.q_count
    print("Quick Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Quick Sort data to the file
    write_file.write_to_file('Quick Sort', 'O(n^2)', 'O(nlog(n))', 1000, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)

    # 10000 list
    first_list, second_list, third_list, fourth_list = arrayGenerator.generate_random_list_number(10000)
    print("{}, {}, {}, {}".format(len(first_list), len(second_list), len(third_list), len(fourth_list)))

    # sorting 10000 list with bubblesort
    start_time = time.perf_counter()
    first_list, comparisons = bubbleSort.bubble_sort(first_list)
    end_time = time.perf_counter()
    print("Bubble Sort time: %s seconds" % (end_time - start_time))
    print("Bubble Sort comparisions: ", comparisons)

    # Creating the semisorted list
    first_list = arrayGenerator.randomizer(first_list)

    # sorting 10000 semisorted list with bubblesort
    start_time_semisorted = time.perf_counter()
    first_list, semisorted_comparisons = bubbleSort.bubble_sort(first_list)
    end_time_semisorted = time.perf_counter()
    print("Bubble Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    print("Bubble Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Bubble Sort data to the file
    write_file.write_to_file('Bubble Sort', 'O(n^2)', 'O(n)', 10000, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)

    # sorting 10000 list with selectionsort
    start_time = time.perf_counter()
    second_list, comparisons = selectionSort.selection_sort(second_list)
    end_time = time.perf_counter()
    print("Selection Sort time: %s seconds" % (end_time - start_time))
    print("Selection Sort comparisions: ", comparisons)

    # Creating the semisorted list
    second_list = arrayGenerator.randomizer(second_list)

    # sorting 10000 semisorted list with selectionsort
    start_time_semisorted = time.perf_counter()
    second_list, semisorted_comparisons = selectionSort.selection_sort(first_list)
    end_time_semisorted = time.perf_counter()
    print("Selection Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    print("Selection Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Selection Sort data to the file
    write_file.write_to_file('Selection Sort', 'O(n^2)', 'O(n^2)', 10000, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)
    
    # sorting 10000 list with mergesort
    start_time = time.perf_counter()
    third_list = merge_sort.merge_sort(third_list)
    end_time = time.perf_counter()
    print("Merge Sort time: %s seconds" % (end_time - start_time))
    print("Merge Sort comparisions: ", merge_sort.count)

    # Creating the semisorted list
    third_list = arrayGenerator.randomizer(third_list)

    # sorting 10000 semisorted list with mergesort
    start_time_semisorted = time.perf_counter()
    third_list = merge_sort.merge_sort(third_list)
    end_time_semisorted = time.perf_counter()
    print("Merge Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    semisorted_comparisons = merge_sort.count
    print("Merge Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Merge Sort data to the file
    write_file.write_to_file('Merge Sort', 'O(nlog(n))', 'O(nlog(n))', 10000, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)

    # sorting 10000 list with quicksort
    start_time = time.perf_counter()
    quickSort.quick_sort(fourth_list)
    end_time = time.perf_counter()
    print("Quick Sort time: %s seconds " % (end_time - start_time))
    comparisons = quickSort.q_count
    print("Quick Sort comparisions: ", quickSort.q_count)

    # Creating the semisorted list
    fourth_list = arrayGenerator.randomizer(fourth_list)

    # sorting 10000 semisorted list with quicksort
    start_time_semisorted = time.perf_counter()
    quickSort.quick_sort(fourth_list)
    end_time_semisorted = time.perf_counter()
    print("Quick Sort time on semisorted array: %s seconds" % (end_time_semisorted - start_time_semisorted))
    semisorted_comparisons = quickSort.q_count
    print("Quick Sort comparisions on semisorted array: ", semisorted_comparisons)

    # Writing the Quick Sort data to the file
    write_file.write_to_file('Quick Sort', 'O(n^2)', 'O(nlog(n))', 10000, end_time - start_time, comparisons, end_time_semisorted - start_time_semisorted, semisorted_comparisons)

    write_file.close()

if __name__ == "__main__":
    main()
