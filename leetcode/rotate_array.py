"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
"""Solutions 1"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Time Complexity: O(n), Space:O(n)"""
        pointer = k%len(nums)

        nums[:] = nums[-pointer:] + nums[:-pointer]

        return nums

"""Solution 2"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Time Complexity: O(n), Space:O(1)"""
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        # temp = 0

        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            end -= 1
            start += 1