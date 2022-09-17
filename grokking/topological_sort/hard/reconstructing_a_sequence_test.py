import pytest


def can_construct(original_seq, sequences):
    """
    Given a sequence `original_seq` and an array of sequences,
    write a method to find if `original_seq` can be uniquely
    reconstructed from the array of sequences.

    Unique reconstruction means that we need to find if
    `original_seq` is the only sequence such that all sequences
    in the array are subsequences of it.

    Solution:
        Run function for finding all topological sorts,
        if count is >1 return False ans stop
        if count == 1 and order is equal to original_seq return True
    """
    if not len(original_seq):
        return False

    adj_list = {}
    in_degree = {}
    for sequence in sequences:
        for num in sequence:
            in_degree[num] = 0
            adj_list[num] = []

    for seq in sequences:
        for i in range(len(seq) - 1):
            src, dest = seq[i], seq[i + 1]
            in_degree[dest] += 1
            adj_list[src].append(dest)

    # if we don't have ordering rules for all the numbers
    # we'll not able to uniquely construct the sequence
    if len(in_degree) != len(original_seq):
        return False

    sources = [node for node in in_degree if in_degree[node] == 0]
    sorted_order = []
    sorted_order_count = 0
    has_original_seq = False

    def _find_all_topological_sorts(sources):
        nonlocal sorted_order_count
        nonlocal has_original_seq
        if sorted_order_count > 1:
            return

        for source in sources:
            next_sources = list(filter(lambda s: s != source, sources))

            sorted_order.append(source)
            for child in adj_list[source]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    next_sources.append(child)

            _find_all_topological_sorts(next_sources)

            sorted_order.pop()
            for child in adj_list[source]:
                in_degree[child] += 1

        if len(sorted_order) == len(in_degree):
            sorted_order_count += 1
            has_original_seq = has_original_seq or sorted_order == original_seq

    _find_all_topological_sorts(sources)
    return has_original_seq if sorted_order_count == 1 else False


def can_construct_simpler(original_seq, sequences):
    """
    Solition:
        Simple topological sort,
        return False if we have len(sources) > 1, because it leads to multi topo sorts
        return False early as soon sorted_order new element doesn't match original_seq
    """
    if not len(original_seq):
        return False

    adj_list = {}
    in_degree = {}
    for sequence in sequences:
        for num in sequence:
            in_degree[num] = 0
            adj_list[num] = []

    for seq in sequences:
        for i in range(len(seq) - 1):
            src, dest = seq[i], seq[i + 1]
            in_degree[dest] += 1
            adj_list[src].append(dest)

    # if we don't have ordering rules for all the numbers
    # we'll not able to uniquely construct the sequence
    if len(in_degree) != len(original_seq):
        return False

    sources = [node for node in in_degree if in_degree[node] == 0]
    sorted_order = []

    while sources:
        if len(sources) > 1:
            return False

        source = sources.pop()
        if original_seq[len(sorted_order)] != source:
            return False

        sorted_order.append(source)
        for child in adj_list[source]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == len(original_seq)


@pytest.mark.parametrize(
    "original_seq, sequences, expected",
    [
        ([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]], True),
        ([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]], False),
        ([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]], True),
    ],
)
def test_can_construct(original_seq, sequences, expected):
    assert can_construct(original_seq, sequences) == expected
    assert can_construct_simpler(original_seq, sequences) == expected
