"""
961. N-Repeated Element in Size 2N Array
Easy

717

268

Add to List

Share
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3
Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2
Example 3:

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
 

Constraints:

2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 104
nums contains n + 1 unique elements and one of them is repeated exactly n times.
"""

# Solution 1
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time
        # Complexity: O(n), Space: O(n)
        n = len(nums) // 2

        hash_map = {}

        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        for key, value in hash_map.items():
            if value == n:
                return key

#  Solution 2: Faster, as no additional memory used
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums) // 2

        for i in nums:
            if nums.count(i) == n:
                return i