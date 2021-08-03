class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        #       Time Complexity: O(n^2) Space: O(n)
        res = []

        for i in range(len(queries)):
            index = queries[i][1]
            nums[index] = nums[index] + queries[i][0]
            idx = 0
            sums = 0

            while idx < len(nums):
                if nums[idx] % 2 == 0:
                    sums += nums[idx]

                idx += 1

            res.append(sums)

        if len(res) == 0:
            res.append(0)

        return res


