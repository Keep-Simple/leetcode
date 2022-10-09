import pytest


def combination_sum(candidates, target):
    """
    https://leetcode.com/problems/combination-sum

    Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen numbers sum to target.
    You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times.
    Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations
    that sum up to target is less than 150 combinations for the given input.

    Constraints:
        1 <= candidates.length <= 30
        2 <= candidates[i] <= 40
        All elements of candidates are distinct.
        1 <= target <= 500

    Solution:
        Do backtracking (stateful dfs) over sorted candidates
        Use min_candidate_idx to prevent duplicates like
        2, 2, 3 & 2, 3, 2
        by now allowing smaller candidates than current,
        because we already checked it previously

        When diff is >= 0, do a backtrack step by removing the last
        element from combination
    """
    candidates.sort()
    n = len(candidates)
    ans = []

    def dfs(target, combination, min_candidate_idx):
        for i in range(min_candidate_idx, n):
            candidate = candidates[i]
            diff = target - candidate
            if diff < 0:
                break

            combination.append(candidate)
            if diff == 0:
                ans.append(combination.copy())
                combination.pop()  # backtrack
                break

            if diff > 0:
                dfs(diff, combination, i)
                combination.pop()  # backtrack

    dfs(target, [], 0)
    return ans


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ],
)
def test_combination_sum(candidates, target, expected):
    assert combination_sum(candidates, target) == expected
