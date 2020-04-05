import pytest
import inspect

from efficient_dedup import deduplication_algorithms
from efficient_dedup.efficient_deduplication import EfficientDeduplicator, SortingAlgorithm, DeduplicationAlgorithm


class TestEfficientDeduplicators:
    def test_deduplicate_efficiently_basic(self):
        sorter = SortingAlgorithm()
        deduplicator = DeduplicationAlgorithm()
        efficient_deduplicator = EfficientDeduplicator(sorter, deduplicator)

        list_with_duplicates = [1, 2, 2, 7, 4, 8, 9, 3, 5, 4, 6, 3, 1, 7, 3, 3]

        assert set(efficient_deduplicator.deduplicate_efficiently(list_with_duplicates)) == set(list_with_duplicates)

    @pytest.mark.parametrize('list_with_duplicates',
                             [
                                 [1, 2, 2, 7, 4, 8, 9, 3, 5, 4, 6, 3, 1, 7, 3, 3],
                                 [1, 2, 3, 5, 7, 9, 4, 7, 8],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1]
                             ])
    def test_deduplicate_efficiently_w_data_parametrization(self,
                                                            list_with_duplicates):
        sorter = SortingAlgorithm()
        deduplicator = DeduplicationAlgorithm()
        efficient_deduplicator = EfficientDeduplicator(sorter, deduplicator)

        assert set(efficient_deduplicator.deduplicate_efficiently(list_with_duplicates)) == set(list_with_duplicates)

    @pytest.mark.parametrize('list_with_duplicates',
                             [
                                 [1, 2, 2, 7, 4, 8, 9, 3, 5, 4, 6, 3, 1, 7, 3, 3],
                                 [1, 2, 3, 5, 7, 9, 4, 7, 8],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1]
                             ])
    @pytest.mark.parametrize('sorting_algorithm_reverse_option',
                             [
                                 True,
                                 False
                             ])
    @pytest.mark.parametrize('deduplication_algorithm_class',
                             [
                                 getattr(deduplication_algorithms, name)
                                 for name, obj
                                 in inspect.getmembers(deduplication_algorithms)
                                 if inspect.isclass(obj)
                             ])
    def test_deduplicate_efficiently_w_data_and_class_parametrization(self,
                                                                      list_with_duplicates,
                                                                      sorting_algorithm_reverse_option,
                                                                      deduplication_algorithm_class):
        sorter = SortingAlgorithm(reverse=sorting_algorithm_reverse_option)
        deduplicator = deduplication_algorithm_class()
        efficient_deduplicator = EfficientDeduplicator(sorter, deduplicator)

        assert set(efficient_deduplicator.deduplicate_efficiently(list_with_duplicates)) == set(list_with_duplicates)
