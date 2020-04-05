class SortingAlgorithm:
    def __init__(self, reverse=False):
        self.__reverse = reverse

    def sort(self, list_to_sort):
        if self.__reverse:
            list_to_sort.sort(reverse=True)
        else:
            list_to_sort.sort()

        return list_to_sort
