#	mergeSort.py for Algorithms Project 2
#
#  An O(n log n) algorithm
#  Merge sort implements a divide and conquer method of algorithmic design by
#  repeatedly dividing an unsorted list length n in two until n number of 
#  single elements are left. Then conquering the lists, 2 at a time, until 
#  they are all merged into one sorted list.
#  
#  Algorithm used: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
#  Contributed by Ross Adams


class MergeSort:

    def __init__(self):
        self.count = 0

    def merge_sort(self, arr):
        # The last array split
        if len(arr) <= 1:
            return arr
        mid = (len(arr) // 2)
        # Perform merge_sort recursively on both halves
        right = self.merge_sort(arr[mid:])
        left = self.merge_sort(arr[:mid])

        # Merge each side together
        return self.merge(left, right, arr.copy())

    def merge(self, left, right, merged):

        left_cursor, right_cursor = 0, 0
        sorted_cursor = left_cursor
        while left_cursor < len(left) and right_cursor < len(right):

            # Sort each one and place into the result
            if left[left_cursor] <= right[right_cursor]:
                self.count += 1
                merged[sorted_cursor] = left[left_cursor]
                left_cursor += 1
            else:
                self.count += 1
                merged[sorted_cursor] = right[right_cursor]
                right_cursor += 1

        for left_cursor in range(left_cursor, len(left)):
            merged[sorted_cursor] = left[left_cursor]
            sorted_cursor += 1

        for right_cursor in range(right_cursor, len(right)):
            merged[sorted_cursor] = right[right_cursor]
            sorted_cursor += 1

        return merged