"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""


def solution(s, k):
    p1 = 0
    counter = 0
    curr_sum = 0
    final_sum = 0

    for idx, val in enumerate(s):

        if counter < k:
            curr_sum = curr_sum + val
            if final_sum < curr_sum:
                final_sum = curr_sum
            counter += 1
        else:
            curr_sum = curr_sum - s[p1]
            curr_sum = curr_sum + val
            p1 += 1
            if final_sum < curr_sum:
                final_sum = curr_sum

    return final_sum


print(solution([2, 3, 4, 1, 5], 2))
