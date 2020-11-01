"""
Maximum Subarray Problem
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Time Complexity: O(n), Space O(1)
"""


def maxSubArray(self, nums: List[int]) -> int:
    current = 0
    maximum = nums[0]
    start_pointer = last_pointer = int_pointer = 0

    if len(nums) - 1 == 0:
        return nums[0]

    for i in range(0, len(nums)):
        current = current + nums[i]
        if maximum < current:
            maximum = current
            start_pointer = int_pointer
            last_pointer = i

        if current < 0:
            current = 0
            int_pointer = i + 1

    return maximum