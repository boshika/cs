class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Time Complexity: O(n) Spca Complexity:O(n)"""
        p1 = 0
        d = {}
        curr_length, final_length = 0, 0

        for idx, val in enumerate(s):
            if val in d and d[val] >= p1:
                p1 = 1 + d[val]
                curr_length = idx - d[val]
                d[val] = idx
            else:
                d[val] = idx
                curr_length += 1
                if curr_length > final_length:
                    final_length = curr_length

        return final_length
