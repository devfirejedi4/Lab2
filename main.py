# Create a welcome message.
# Input: a name as a string.
# Result: a string.
def welcome_message(name: str) -> str:
    message = "Hello, " + name + "!"
    return message


message = welcome_message("dromer35@calpoly.edu")
print(message)

def smallest(n:float,m:float) -> float:
    if n<m:
        return n#first
    else:
        return m
first = smallest(3,2)#2
second = smallest(2,2)#2 why reasonable since 2 is the smallest number avaible, is a bit unreasonable due to being the same number
print()

def function2(a:int, b:int, c:int)->int:
    if a>b and a>c:#when a is the biggest number
        return a-b
    elif b>c:#when A isn't the biggest number and B is bigger than C
        return b+c
    else:#when A and B aren't the biggest numbers, so C is
        return 2*c

ans1 = function2(3,2,1)#1
ans2 = function2(2,3,1)#4
ans3 = function2(2,1,3)#6
print()

def checked_access(L:list[int], idx:int):#optional[int]:
    test = idx >= 0 and idx < len(L)#first = false and second = true
    if test:#this is checking to see of idx is out of the bounds of the list
        return L[idx]
    else:
        return None
first = checked_access([1, 0, 1], 9)#none
second = checked_access([1,0,1], 2)#1
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:#first, this, is, the
        result = len(L[0]) + len(L[1]) + len(L[2])
    elif len(L) > 1:#third, another, call
        result = len(L[0]) + len(L[1])
    elif len(L) > 0:
        result = len(L[0])# second, second call
    else:
        result = 0
    return result
first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def suprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L
words = ["this","is","confusing","code."]
first = suprising(words, "Avoid")
second = suprising(words, "such.")
#words is the same
#first has words with "AVOID" and second has words with "AVOID" as well as "SUCH"
#suprising added aviod and such to words and capitalized both of them
print()
