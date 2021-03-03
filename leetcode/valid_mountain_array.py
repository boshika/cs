"""VALID MOUNTAIN ARRAY
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""

"""Time Complexity: O(n), Space Complexity:O(n), since slicing"""
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        pinnacle = max(arr)
        pinnacle_index = arr.index(pinnacle)

        left_of_pinnacle = arr[0:pinnacle_index + 1]
        right_of_pinnacle = arr[pinnacle_index:]

        if len(arr) >= 3:
            if len(left_of_pinnacle) <= 1 or len(right_of_pinnacle) <= 1:
                return False

            for idx in range(len(left_of_pinnacle) - 1):
                if left_of_pinnacle[idx] >= left_of_pinnacle[idx + 1]:
                    return False

            for idx in range(len(right_of_pinnacle) - 1):
                if right_of_pinnacle[idx] <= right_of_pinnacle[idx + 1]:
                    return False
        else:
            return False

        return True

"""Leetcode Solution
   Time Complexity: O(n), Space: O(1)
"""


def validMountainArray(self, A):
    N = len(A)
    i = 0

    # walk up
    while i + 1 < N and A[i] < A[i + 1]:
        i += 1

    # peak can't be first or last
    if i == 0 or i == N - 1:
        return False

    # walk down
    while i + 1 < N and A[i] > A[i + 1]:
        i += 1

    return i == N - 1