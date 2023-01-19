# Create a welcome message.
# Input: a name as a string.
# Result: a string.
def welcome_message(name: str) -> str:
    message = "Hello, " + name + "!"
    return message


message = welcome_message("cmkwon128@gmail.com")
print(message)

#lab 2 task 3
print("lab 2 task 3")
def smallest(n:float, m:float) -> float:
     if n < m:             #if n is less then m, then  return n
         return n          #if n is equal or greater than m, then return m
     else:
         return m

first = smallest(3,2)     #value of first is 2
second = smallest(2,2)       #value of second is 2, this is reasonable because when n = m, then it returns m which m is 2 also.
print("first = ",first, " second = ", second)

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c: #when a is greater then both b and c
        return a-b
    elif b>c: #when a is less than or equal to b and/or c and when b is greater than c
        return b+c
    else: #when a is less than or equal to b and/or c and when b is less than or equal to c.
        return 2*c

answer1 = function2(3,2,1) #answer 1 = 1
answer2 = function2(2,3,1) #answer 2 = 4
answer3 = function2(2,1,3) #answer 3 = 6
print(" answer1 = ", answer1, " answer2 = ", answer2, " answer3 = ", answer3)

#lab 2 task 4
print("")
print("lab 2 task 4")

from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L) #the value of test is greater than or equal to 0 and is the second variable inputed in the function.
    if test: #this check prevents any negative value of test to be used and to make sure idx < len(L)
        return L[idx]
    else:
        return None

first = checked_access([1,0,1], 9) #first = None
second = checked_access([1,0,1], 2) #second = 1
print("first = ", first, " second = ", second)

