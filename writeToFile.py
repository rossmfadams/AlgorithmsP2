# This class write name, best case, worst case, unsorted time, unsorted counter,
# semi sorted time, and semi sorted counter to a file call data.txt
#


class WriteToFile:
    def __init__(self):
        self.fileOpen = open('data.txt', 'w')

    def write_to_file(self, name, worst_case, best_case, unsorted_time, unsorted_counter, semi_sorted_time, semi_sorted_counter):
        self.fileOpen.write('Best Case for ' + name + ': ' + best_case + '\n')
        self.fileOpen.write('Worst Case for ' + name + ': ' + worst_case + '\n')
        self.fileOpen.write('The time for unsorted is: {} \n'.format(unsorted_time))
        self.fileOpen.write('The unsorted counter for ' + name + 'is: {}'.format(unsorted_counter))
        self.fileOpen.write('The time for semi sorted is: {} \n'.format(semi_sorted_time))
        self.fileOpen.write('The unsorted counter for ' + name + 'is: {}'.format(semi_sorted_counter))
