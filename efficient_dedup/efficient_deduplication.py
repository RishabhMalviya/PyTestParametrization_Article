from .deduplication_algorithms import DeduplicationAlgorithm
from .sorting_algorithms import SortingAlgorithm


class EfficientDeduplicator:
    def __init__(self, sorting_algorithm: SortingAlgorithm, deduplication_algorithm: DeduplicationAlgorithm):
        self.__sorting_algorithm = sorting_algorithm
        self.__deduplication_algorithm = deduplication_algorithm

    def deduplicate_efficiently(self, list_to_deduplicate):
        return self.__deduplication_algorithm.deduplicate(self.__sorting_algorithm.sort(list_to_deduplicate))
