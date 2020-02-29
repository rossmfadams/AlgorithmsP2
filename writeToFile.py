# This class write name, best case, worst case, unsorted time, unsorted counter,
# semi sorted time, and semi sorted counter to a file call data.txt
#


class WriteToFile:
    def __init__(self):
        self.fileOpen = open('data.txt', 'w')

    def write_to_file(self, name, worst_case, best_case, num_elements, unsorted_time, unsorted_counter, semi_sorted_time, semi_sorted_counter):
        self.fileOpen.write(name + ': ')
        self.fileOpen.write('\nBest Case for ' + name + ': ' + best_case + '\n')
        self.fileOpen.write('Worst Case for ' + name + ': ' + worst_case + '\n')
        self.fileOpen.write('Number of elements sorted: {}'.format(num_elements))
        self.fileOpen.write('\nThe time for unsorted ' + name + ' is: {} \n'.format(unsorted_time))
        self.fileOpen.write('The unsorted counter for ' + name + ' is: {}\n'.format(unsorted_counter))
        self.fileOpen.write('The time for semi sorted ' + name + ' is: {} \n'.format(semi_sorted_time))
        self.fileOpen.write('The unsorted counter for semi sorted ' + name + ' is: {}\n\n\n'.format(semi_sorted_counter))

    def close(self):
        self.fileOpen.close()
