#  quickSort.py for Algorithms Project 2
#
#  An O(n log n) algorithm
#  Quick sort defines a pivot element and moves all smaller elements to the 
#  left and larger elements to the right. Then recursively repeats those 
#  steps to the left and right subarrays using smaller/bigger pivots 
#  respectively
#  
#  Algorithm used: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
#  Contributed by Ross Adams
q_count = 0

def partition(array, begin, end):
    global q_count
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            q_count +=1
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    global q_count
    if begin >= end:
        q_count += 1
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)
    

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)