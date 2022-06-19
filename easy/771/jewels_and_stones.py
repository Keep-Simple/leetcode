class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_count_map = {j: 0 for j in jewels}

        for s in stones:
            if s in jewels_count_map:
                jewels_count_map[s] += 1

        return sum(jewels_count_map.values())
