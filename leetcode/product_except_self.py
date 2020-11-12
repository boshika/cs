"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
"""

"""Solution 1"""
class Solution:
    """Time Complexity O(n), Space: O(n)"""
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)

        left, right = [0] * nums_length, [0] * nums_length

        left[0] = 1
        right[-1] = 1

        # Traverse Left Side
        for i in range(1, nums_length):
            left[i] = left[i - 1] * nums[i - 1]

        # Traverse Right Side
        for j in reversed(range(nums_length - 1)):
            right[j] = right[j + 1] * nums[j + 1]

        answer = [left * right for left, right in zip(left, right)]

        return answer

"""Solution 2"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Time Complexity: O(n), Space: O(1)"""
        nums_length = len(nums)

        left, right = [0] * nums_length, [0] * nums_length

        left[0] = 1
        right[-1] = 1

        # Traverse Left Side
        for i in range(1, nums_length):
            left[i] = left[i - 1] * nums[i - 1]

        R = 1;
        for i in reversed(range(nums_length)):
            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            left[i] = left[i] * R
            R *= nums[i]

        return left

