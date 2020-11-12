"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Time Complexity: O(n), Space:O(n) dues to the usage of set"""
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
        nums = set(nums)

        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = nums[i]
            elif i > max3:
                max3 = i

        if len(nums) < 3:
            return max1

        return max3
