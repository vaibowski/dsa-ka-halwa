from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    price = [0]*(len(cost)+1)

    for i in range(len(cost)-1):
        price[i+2] = min((cost[i]+price[i]), (cost[i+1]+price[i+1]))

    return price[-1]