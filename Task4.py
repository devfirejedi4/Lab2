from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)  #  Value of first is False. Value of second is True.
    if test:                          #  This check is preventing index for being > list length, and for index being a negative number.
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)  #  Value = None.
second = checked_access([1, 0, 1], 2)  #  Value = 1. Second index value.
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])  #This is being evaluated if the length of the list is > 2
    elif len(L) > 1:
        result = len(L[0]) + len(L[1])  #  This is being evaluated if length is 2
    elif len(L) > 0:
        result = len(L[0])  #  This is being evaluated if length is 1
    else:
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()


def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         #What is the value of words at this point? ['this', 'is', 'confusing', 'code']
         # What are the values of first and second at this point?
         # first = ['this', 'is', 'confusing', 'code', 'AVOID'].
         # second = ['this', 'is', 'confusing', 'code', 'AVOID', 'such']
         # What happened? The words in the parameter got appended to the original list, without creating a new list.

print(first)





