#	selectionSort.py for Algorithms Project 2
#
#  A O(n^2) algorithm
#  Selection sort creates two lists sorted and unsorted by selecting the
#  smallest element from the unsorted list and placing it at the end of 
#  of the sorted list.
#  
#  Algorithm used: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
#  Contributed by Ross Adams

def selection_sort(arr):
	comparisons = 0
	for i in range(len(arr)):
		minimum = i

		for j in range(i + 1, len(arr)):
			comparisons += 1
			# Select the smallest value
			if arr[j] < arr[minimum]:
				minimum = j

        # Place it at the front of the
        # sorted end of the array
		arr[minimum], arr[i] = arr[i], arr[minimum]

	return arr, comparisons