#  bubbleSort.py for Algorithms Project 2
#  O(n^2) Sorting Algorithm
#  Bubble Sort which will take the list and sort it by switching the numbers 
#  when they are greater than the previous number and continue doing this until 
#  the list is sorted
#  Bubble Sort Algorithm used: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
#  Contributed by Riley Williams

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