from collections import defaultdict

import pytest


def find_order(words):
    """
    There is a dictionary containing words from an alien language
    sorted lexicographically
    for which we don’t know the ordering of the letters.
    Write a method to find the correct order of the letters in the alien language.
    It is given that the input is a valid dictionary
    and there exists an ordering among its letters.

    Solution:
        - build a adjacency list for each node (using the fact that words are sorted lexicographically)
        - use bfs topological sort to find the ordering


    TC and SC:
        V = number of different characters
        E = total number of rules, each words pair give us one rule
            so E = N, where N is the number of words
        O(V+N)
    """
    n = len(words)
    if n == 0:
        return ""

    adj_list = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    for i in range(n - 1):
        prev_word, curr_word = words[i], words[i + 1]
        # compare adjacent words, find first distinct letter
        # and use it to build adj_list
        for l1, l2 in zip(prev_word, curr_word):
            if l1 != l2:
                # make sure we don't duplicate dependencies
                if l2 not in adj_list[l1]:
                    adj_list[l1].add(l2)
                    in_degree[l2] += 1
                break

    sources = [node for node in in_degree if in_degree[node] == 0]
    sorted_order = []

    while sources:
        source = sources.pop()
        sorted_order.append(source)
        for child in adj_list[source]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # has a cycle
    if len(sorted_order) != len(in_degree):
        return ""

    return "".join(sorted_order)


@pytest.mark.parametrize(
    "words, expected",
    [
        (["ba", "bc", "ac", "cab"], "bac"),
        (["cab", "aaa", "aab"], "cab"),
        (["ywx", "wz", "xww", "xz", "zyy", "zwz"], "ywxz"),
    ],
)
def test_find_order(words, expected):
    assert find_order(words) == expected
