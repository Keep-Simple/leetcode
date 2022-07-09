import pytest


def find_happy_number(num):
    """
    Any number will be called a happy number if,
    after repeatedly replacing it with a number equal
    to the sum of the square of all of its digits, leads us to number ‘1’.
    All other (not-happy) numbers will never reach ‘1’. Instead,
    they will be stuck in a cycle of numbers which does not include ‘1’.
    """
    ptr1 = ptr2 = num
    while True:
        ptr1 = digit_square_sum(ptr1)
        ptr2 = digit_square_sum(digit_square_sum(ptr2))

        if ptr1 == 1 or ptr2 == 1:
            return True

        if ptr1 == ptr2:
            return False


def digit_square_sum(num):
    sum = 0
    while num != 0:
        d = num % 10
        num //= 10
        sum += d**2
    return sum


@pytest.mark.parametrize("num,expected", [(23, True), (12, False)])
def test(num, expected):
    assert find_happy_number(num) == expected
