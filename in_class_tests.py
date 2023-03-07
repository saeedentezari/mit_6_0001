
import time

#########################################################
# Towers of Hanoi

def printMove(disk, fr, to):
    # print('move from ' + str(fr) + ' to ' + str(to))
    print(f'move disk {disk} from {fr} to {to}')

call_counter = [0]
def moveTowers(h, fr, to, spare, disk=None):
    call_counter[0] += 1
    if h == 1:
        printMove(disk, fr, to)
    else:
        moveTowers(h-1, fr, spare, to, disk=1)
        moveTowers(1, fr, to, spare, disk=h)
        moveTowers(h-1, spare, to, fr, disk=1)

# moveTowers(3, 0, 1, 2)
# print(call_counter[0])

#########################################################
# Palindrome

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        cleaned = ''
        for char in s:
            if char.isalpha():
                cleaned += char
        return cleaned

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

# s = 'cAble was I, ere I saw Elba'
# print(isPalindrome(s))

#########################################################
# Fibonacci

# (a) Inefficient
counter = [0]
def fib(n):
    counter[0] += 1
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# n = 10
# print(fib(n))
# print(counter)
# # number of calls needed for eval fib(n) = C(n) = 2 * fib(n+1) - 1
# # notice the first terms convention (here fib(0) = 0, fib(1) = 1)
# print(fib(n+1))       
                    

# (b) Efficient
counter = [0]
def fib_efficient(n, memo):
    counter[0] += 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_efficient(n-1, memo) + fib_efficient(n-2, memo)
        return memo[n]

memo = {0: 0, 1: 1}
# print(fib_efficient(5, memo))
# print(counter)

###############################################################
# OOP

class Coordinate(object):

    def __init__(self, x, y):
        
        self.x = x
        self.y = y

    def distance(self, other):
        
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**(1/2)

    def __str__(self):

        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def __add__(self, other):

        return Coordinate(self.x + other.x, self.y + other.y)

# origin = Coordinate(0, 0)
# c = Coordinate(3, 4)
# b = Coordinate(1, 2)
# print(origin.distance(c))
# print(Coordinate.distance(c, origin))
# print(c)
# print(type(c))
# print(type(Coordinate))
# print(isinstance(c, Coordinate))
# print(c + b)

class Fraction(object):

    def __init__(self, num, denom):

        assert type(num) == int and type(denom) == int
        assert denom != 0
        self.num = num
        self.denom = denom

    def __str__(self):

        return str(self.num) + '/' + str(self.denom)

    def __add__(self, other):

        denom = self.denom * other.denom
        num = self.num * other.denom + self.denom * other.num
        return Fraction(num, denom)

    def __sub__(self, other):

        denom = self.denom * other.denom
        num = self.num * other.denom - self.denom * other.num
        return Fraction(num, denom)

    def __float__(self):

        return self.num / self.denom

    def inverse(self):

        return Fraction(self.denom, self.num)

# a = Fraction(1, 4)
# b = Fraction(3, 4)
# print(a - b)
# print(a)
# print(float(a))
# print(a.inverse())
# print(a.denom)

class Rabit(object):
    
    tag = 1

    def __init__(self, name):
        self.name = name
        self.rid = Rabit.tag
        Rabit.tag += 1

# print(Rabit.tag)
# r1 = Rabit('Angela')
# print(r1.rid)
# print(Rabit.tag)
# r2 = Rabit('Ronia')
# print(r2.rid)
# print(Rabit.tag)

###############################################################
# Order of Growth


# ================== Bisection Search =========================

# Implementation 1
# O(n log n)
# -> in fact O(n), if we want to be careful in calculating the complexity


def bisection_search1(L, e):

    # base cases
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    # recursive case
    else:
        mid = len(L) // 2
        if e < L[mid]:
            return bisection_search1(L[:mid], e)
        else:
            return bisection_search1(L[mid:], e)

# Implementation 2
# O(log n)

def bisection_search2(L, e):

    start = 0
    end = len(L) - 1

    def bisection_search_helper(L, e, start, end):

        # base cases
        if start == end:
            return L[start] == e
        # recursive case
        else:
            mid = (start + end + 1) // 2
            if e < L[mid]:
                end = mid - 1
                return bisection_search_helper(L, e, start, end)
            else:
                start = mid
                return bisection_search_helper(L, e, start, end)

    return bisection_search_helper(L, e, start, end)

# n = 10**4
# n = n**2
# # n = 2 * n 
# sorted_list = [0]*n
# e = -1

# t0 = time.time()
# print(bisection_search2(sorted_list, e))
# t1 = time.time()
# print(t1 - t0)


# ======= int to str, another logarithmic complexity ==========

def intToStr(i):
    
    digits = '0123456789'
    
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    
    return result

# i = 10**40
# t0 = time.time()
# print(intToStr(i))
# t1 = time.time()
# print(t1 - t0)


# =========== Power Set: All subsets of a set =================

def powerSet(L):

    # base case
    if len(L) == 0:
        return [[]]

    # recursive case
    else:
        # get the previous powerset (powerset of L except the last element) as a list of sets
        prevPowSet = powerSet(L[:-1])
        # print(prevPowSet)
        # and keep apart the set of last element
        lastEleSet = L[-1:]
        # we can obtain powerset of L+ele by adding and not adding ele to each set in powerset of L
        # or powerset(L) = powerset(L-lastele) + all sets of powerset(L-lastele) appended by lastele
        return prevPowSet + [Set+lastEleSet for Set in prevPowSet]

# print(powerSet([1, 2, 3, 4]))



################################################################
# Searching and Sorting

L = [1, 3, 2, 5, 4, 0]



def bubble_sort(L):

    had_swap = True     # for enter to while loop
    while had_swap:
        print('list L is now:', L)
        # swap flag
        had_swap = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]     # swapping
                had_swap = True
    return L    # sorted list

# print('the final sorted list:', bubble_sort(L))

def selection_sort(L):

    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt+1, len(L)):
            if L[suffixSt] > L[i]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

    return L

# print(selection_sort(L))


# ========= Merge Sort ===========

def merge(left, right):

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if i < len(left):
        result.extend(left[i:])
    else:
        result.extend(right[j:])

    return result


# left = [0, 2, 4, 6]
# right = [1, 3, 4, 5, 7]
# print('merged result', merge(left, right))


def merge_sort(L):

    # base case
    if len(L) < 2:
        return L[:]

    # recursive case
    else:
        # divide
        mid = len(L) // 2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        # conquer
        return merge(left, right)


L = [8, 4, 6, 2, 7, 3, 4, 1, 0, 9, 5]
print('sort result', merge_sort(L))