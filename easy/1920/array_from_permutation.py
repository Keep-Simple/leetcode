from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Solve without extra memory - time:O(N) space:O(1)

        Modify nums such that nums[i] contains initial value & final value
        nums[i] // n == final val
        nums[i] % n == initial val
        """
        n = len(nums)

        for i in range(n):
            b = nums[nums[i]] % n
            nums[i] += n * b

        for i in range(n):
            nums[i] = nums[i] // n

        return nums

    def buildArraySimple(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
