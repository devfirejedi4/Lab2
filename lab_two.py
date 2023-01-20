def smallest(n: float, m: float) -> float:
    if n < m:
        return n
    else:
        return m

    first = smallest(3, 2)
    # the result of first is m
    second = smallest(2, 2)
    # the result of second is also m

    print()


def function2(a: int, b: int, c: int) -> float:
    if a > b and a > c:
        return a - b
    # a call to this function will evaluate this statement when a is greater than all the other values

    elif b > c:
        return b + c
    # a call that evaluates this will happen when a is not greater than b or c and b is more than c

    else:
        return 2 * c
    # this is for all other options


answer1 = function2(3, 2, 1)
# 1

answer2 = function2(2, 3, 1)
# 4

answer3 = function2(2, 1, 3)
# 6


from typing import Optional


def checked_access(L: list[int], idx: int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)
    # the value of test on each call is
    if test:
        return L[idx]
    else:
        return none


first = checked_access([1, 0, 1], 9)
second = checked_access([1, 0, 1], 2)
