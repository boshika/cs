"""
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Time Complexity: O(n) time, O(1) space
"""


def maxProfit(prices):
    if len(prices) == 0:
        return 0

    min_price = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        profit = max(profit, prices[i] - min_price)

    return profit