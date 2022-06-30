from typing import DefaultDict


def longest_substring_with_k_distinct(string, k):
    substring_dict = DefaultDict(int)
    max_len, window_start = 0, 0
    for window_end in range(len(string)):
        substring_dict[string[window_end]] += 1

        while len(substring_dict) > k:
            substring_dict[string[window_start]] -= 1
            if substring_dict[string[window_start]] <= 0:
                del substring_dict[string[window_start]]
            window_start += 1

        max_len = max(window_end - window_start + 1, max_len)

    return max_len
