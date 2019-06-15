import math

def is_perfect_square(n):
    """Given an integer, return whether or not it is a perfect square

    Specifically, this means that there is a real integer such that i*i == n
    """

    s = math.sqrt(n)
    return s == int(s)


def is_perfect_square_fixed(n):
    """Given an integer, return whether or not it is a perfect square

    Specifically, this means that there is a real integer such that i*i == n
    """

    # Negative numbers are not squares given the definition of the function
    if n < 0:
        return False

    s = math.sqrt(n)
    return s == int(s)
