import pytest

from grokking.two_heaps.utils import MaxHeap, MinHeap


def find_maximum_capital(capitals, profits, number_of_projects, initial_capital):
    """
    Given a set of investment projects with their respective profits,
    we need to find the most profitable projects.
    We are given an initial capital and are allowed
    to invest only in a fixed number of projects.
    Our goal is to choose projects that give us the maximum profit.
    Write a function that returns the maximum total capital
    after selecting the most profitable projects.

    We can start an investment project only
    when we have the required capital. Once a project is selected,
    we can assume that its profit has become our capital.
    """
    curr_capital = initial_capital
    profits_heap = MaxHeap()
    capitals_heap = MinHeap([[capitals[i], i] for i in range(len(capitals))])

    for _ in range(number_of_projects):
        while len(capitals_heap) and capitals_heap.top()[0] <= curr_capital:
            profits_heap.push(profits[capitals_heap.pop()[1]])
        if len(profits_heap):
            curr_capital += profits_heap.pop()
        else:
            # can't afford to buy anything, break at current project
            break

    return curr_capital


def find_maximum_capital_simple(capitals, profits, number_of_projects, initial_capital):
    curr_capital = initial_capital
    bought_idxs = set()

    for _ in range(number_of_projects):
        max_profit, max_profit_idx = 0, 0
        for i, capital in enumerate(capitals):
            if capital <= curr_capital:
                if max_profit < profits[i] and i not in bought_idxs:
                    max_profit = profits[i]
                    max_profit_idx = i
        bought_idxs.add(max_profit_idx)
        curr_capital += max_profit

    return curr_capital


@pytest.mark.parametrize(
    "capitals, profits, number_of_projects, initial_capital, expected",
    [
        ([0, 1, 2], [1, 2, 3], 2, 1, 6),
        ([0, 1, 2, 3], [1, 2, 3, 5], 3, 0, 8),
        ([0, 1, 1], [1, 2, 3], 2, 0, 4),
    ],
)
def test_find_maximum_capital(
    capitals, profits, number_of_projects, initial_capital, expected
):
    assert (
        find_maximum_capital_simple(
            capitals, profits, number_of_projects, initial_capital
        )
        == expected
    )
    assert (
        find_maximum_capital(capitals, profits, number_of_projects, initial_capital)
        == expected
    )
