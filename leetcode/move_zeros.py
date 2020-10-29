"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Time Complexity: O(n), Space:O(1)
"""

def moveZeroes(nums):
    """
    Space is 99% better, but time is only 49% better. Reason could be
    swapping the o and non zero values could be expensive. See Alternate
    solution
    """
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[p1] = nums[p1], nums[i]

                p1 += 1

        return nums

    def moveZeroes(nums):
        """
        This solution is 100% better in terms of space and 99.49% better in run time
        Instead of swapping, I am just copying the non zero values to the index containing zeros
        At the end, I am adding zeros from where the p2 index starts to the length of the list
        :param nums:
        :return:list
        Time Complexity: O(n), Space: O(1)
        """
        p1 = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p1] = nums[i]

                p1 += 1

        for j in range(p1, len(nums)):
            nums[j] = 0

        return nums
