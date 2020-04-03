class DeduplicationAlgorithm:
    def deduplicate(self, list_with_duplicates):
        return list(set(list_with_duplicates))


class HashSetDeduplicationAlgorithm(DeduplicationAlgorithm):
    def deduplicate(self, list_with_duplicates):
        return {element: True for element in list_with_duplicates}.keys()


class CustomComparisonDeduplicationAlgorithm(DeduplicationAlgorithm):
    def __init__(self, comparison_fun=lambda x, y: x == y):
        self.__comparison_fun = comparison_fun

    def deduplicate(self, list_with_duplicates):
        to_remove = [False]*len(list_with_duplicates)

        for index, element in enumerate(list_with_duplicates):
            if not to_remove[index]:
                to_remove = [True if e == element else to_remove[i] for i, e in enumerate(list_with_duplicates)]

        return [e for i, e in enumerate(list_with_duplicates) if not to_remove[i]]


class LookaheadCustomComparisonDeduplicationAlgorithm(DeduplicationAlgorithm):
    def __init__(self, lookahead_window_size=100, comparison_fun=lambda x, y: x == y):
        self.__lookahead_window_size = lookahead_window_size
        self.__comparison_fun = comparison_fun

    def deduplicate(self, list_with_duplicates):
        to_remove = [False]*len(list_with_duplicates)

        for index, element in enumerate(list_with_duplicates):
            if not to_remove[index]:
                lookahead_window_start = index + 1
                lookahead_window_end = min(index + 100, len(list_with_duplicates))

                to_remove[lookahead_window_start:lookahead_window_end] =\
                    [True if e == element else to_remove[i]
                        for i, e in enumerate(list_with_duplicates[lookahead_window_start:lookahead_window_end])]

        return [e for i, e in enumerate(list_with_duplicates) if not to_remove[i]]
