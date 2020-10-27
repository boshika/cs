"""
TWO NUMBER SUM
Input: [5,3,2,-1,10,1,-3,6], 10
Output: [5,6]

Strategy 1: Brute Force
Loop through the array twice, first loop picks up the initial number,
second loop traverse all the numbers. Compare the the sum to targetsum. If found
return the two values
Time Complexity: Quadratic, Space:O(1)

Strategy 2: Use a Hash Map to track values.
Create a hashmap, traverse the list and check if targetsum-i is in the hashmap
If it is found then return [i, targetsum-i] else set hashmap[i] =0, this just seeting
i as a key in the hash map and giving it some value
Time Complexity: O(n), Space: O(n)
Strategy 3: Sort the Array and Pointer Method
Initially sort the array, then use two pointers one at the start of the array, one at the
end of the array. If value at left pointer + right pointer == targetsum then return
both values.
If value for left pointer + right pointer > targetsum, then decrement right pointer
If value for left pointer + right pointer < targetsum, then increment left pointer
Time Complexity: O(n log n) time, O(1) space
"""


def find_target_sum(array, target_sum):
    """Strategy 2"""
    hashmap = {}

    for i in array:
        value = target_sum-i
        if value in hashmap.keys():
            return [i,value]
        else:
            hashmap[i] = 0
        return []



