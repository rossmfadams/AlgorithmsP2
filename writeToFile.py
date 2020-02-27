class WriteToFile:
    def __init__(self, fileOpen):
        self.fileOpen = open('data.txt', 'w')

    def write_to_file(self, name, worst_case, best_case, unsorted_time, semi_sorted_time, counter):
        self.fileOpen.write('Best Case for ' + name + ': ' + best_case + '\n')
        self.fileOpen.write('Worst Case for ' + name + ': ' + worst_case + '\n')
        self.fileOpen.write('The time for unsorted is: {} \n'.format(unsorted_time))
        self.fileOpen.write('The time for semi sorted is: {} \n'.format(semi_sorted_time))
        self.fileOpen.write('The count for ' + name + 'is: {}'.format(counter))