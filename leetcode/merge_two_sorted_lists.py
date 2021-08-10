"""
Problem Statement #
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).

Input #
Two sorted lists.

Output #
A merged and sorted list consisting of all elements of both input lists.

Sample Input #
list1 = [1,3,4,5]
list2 = [2,6,7,8]
Sample Output #
lst1 = [1,2,3,4,5,6,7,8]
"""

def merge_lists(lst1, lst2):
    p1 = 0
    p2 = 0

    while p1<len(lst1) and p2<len(lst2):
        if lst1[p1]>lst2[p2]:
            lst1.insert(p1, lst2[p2])
            p2+=1
            p1+=1
        else:
            p1+=1
        print(p2)

    if(p2 < len(lst2)):
        lst1.extend(lst2[p2:])
    return lst1