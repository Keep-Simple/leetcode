import pytest


def flip_and_invert_image(matrix):
    """
    Given a binary matrix representing an image,
    we want to flip the image horizontally, then invert it.

    To flip an image horizontally means that each row of the image is reversed.
    For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

    To invert an image means that each 0 is replaced by 1, and each 1
    is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].
    """
    for i in range(len(matrix)):
        reverse_and_invert(matrix[i])
    return matrix


def reverse_and_invert(array):
    start, end = 0, len(array) - 1
    # if len(array) % 2 == 1 -> middle element will still be inverted
    # because start <= end
    while start <= end:
        array[start], array[end] = array[end] ^ 1, array[start] ^ 1
        start += 1
        end -= 1


@pytest.mark.parametrize(
    "matrix, expected",
    [
        (
            [
                [1, 0, 1],
                [1, 1, 1],
                [0, 1, 1],
            ],
            [
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 1],
            ],
        ),
        (
            [
                [1, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 1, 1, 1],
                [1, 0, 1, 0],
            ],
            [
                [1, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 1, 0],
            ],
        ),
    ],
)
def test_flip_and_invert_image(matrix, expected):
    assert flip_and_invert_image(matrix) == expected
