Given
an
array
arr
of
integers, check if there
exists
two
integers
N and M
such
that
N is the
double
of
M(i.e.N = 2 * M).

More
formally
check if there
exists
two
indices
i and j
such
that:

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example
1:

Input: arr = [10, 2, 5, 3]
Output: true
Explanation: N = 10 is the
double
of
M = 5, that is, 10 = 2 * 5.
Example
2:

"""Input: arr = [7, 1, 14, 11]
Output: true
Explanation: N = 14 is the
double
of
M = 7, that is, 14 = 2 * 7.
Example
3:

Input: arr = [3, 1, 7, 11]
Output: false
Explanation: In
this
case
does
not exist
N and M, such
that
N = 2 * M.

Constraints:

2 <= arr.length <= 500
-10 ^ 3 <= arr[i] <= 10 ^ 3
"""
"""Slower Solution
Time Complexity: ???
"""
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = {}
        for i in arr:
            N = i*2
            if N not in d:
                d[N] = 1
            else:
                d[N] += 1
        print(d)
        for i in d:
            print(i)
            if i in arr:
                if i == 0 and d[i] == 2:
                    return True
                elif i != 0 and d[i] == 1:
                    return True
        return False

"""Faster Solution
Time Complexity: O(n)
"""


def checkIfExist(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    d = {j: i for i, j in enumerate(arr)}

    for i in range(len(arr)):
        if arr[i] * 2 in d:
            if d[arr[i] * 2] != i:
                return True
    return False