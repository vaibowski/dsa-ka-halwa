from typing import List


def maxProfit(prices: List[int]) -> int:
    min_cost = pow(10, 4)
    max_profit = 0
    for price in prices:
        min_cost = min(min_cost, price)
        max_profit = max(max_profit, price - min_cost)

    return max_profit
