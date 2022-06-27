# P   A   H   N  0-4-8-12
# A P L S I I G  1357...        n=3
# Y   I   R      2-6-10

# P     I    N   0--6--12
# A   L S  I G   1-5,7-11,13    n=4
# Y A   H R      2,4-8,10
# P     I        3--9


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        is_going_down = False
        row_cursor = 0

        for i in range(len(s)):
            rows[row_cursor] += s[i]
            if i % (numRows - 1) == 0:
                is_going_down = not is_going_down
            row_cursor = row_cursor + 1 if is_going_down else row_cursor - 1

        return "".join(rows)
