"""
Problem Statement #
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So, zero will be placed at the right.

Output #
A list with negative elements at the left and positive elements at the right

Sample Input #
[10,-1,20,4,5,-9,-6]
Sample Output #
[-1,-9,-6,10,20,4,5]
"""
"""Solution 1"""
def rearrange(lst):
"""Time: O(n), Space:(n+m)"""
    neg, pos = [], []

    for i in lst:
        if i>0:
          pos.append(i)
        else:
          neg.append(i)

    return neg+pos

def rearrange(lst):
"""Time: O(n), Space:(1)"""
    leftMostPosEle=0

    for curr in range(len(lst)):
      if (lst[curr] < 0):
        if (curr is not leftMostPosEle):
          lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
        leftMostPosEle += 1

    return lst