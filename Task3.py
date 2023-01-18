def smallest(n:float, m:float) -> float:
    if n < m:
        return n  # It isn't evaluated for either since both times, n is >= m
    else:
        return m

first = smallest(3, 2)  # Value of first is 2
second = smallest(2, 2)  # Value of second is 2. This is not a reasonable result since 2 is not smaller than the other two; they are equivalent in value.
print()


def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b  # Evaluates if a > b and a > c
    elif b > c:
        return b + c  # Evaluates if either a > b or a > c is false
    else:
        return 2 * c  # Evaluates if (a > b or a > c is false) and (c > b)

answer1 = function2(3, 2, 1)  # Value = (3 - 2) = 1
answer2 = function2(2, 3, 1)  # Value = (3 + 1) = 4
answer3 = function2(2, 1, 3)  # Value = (3 * 2) = 6
print()
