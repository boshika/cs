"""
Solution similar to Leetcode solution
Given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
Merge B into A in sorted order.

Examples:

Input : a[] = {10, 12, 13, 14, 18, NA, NA, NA, NA, NA}
        b[] = {16, 17, 19, 20, 22};;
Output : a[] = {10, 12, 13, 14, 16, 17, 18, 19, 20, 22}

Pointer Approach
Time Complexity: O(m+n), O(m+n)
"""


def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p3 = len(nums1) - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p3] = nums2[p2]
            p2 -= 1
        else:
            nums1[p3] = nums1[p1]
            p1 -= 1
        p3 -= 1
    print(nums2[:p2 + 1])
    nums1[:p2 + 1] = nums2[:p2 + 1]

    return nums1

