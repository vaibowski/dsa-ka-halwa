def climbStairs(n: int) -> int:
    stairs = [1]*(n+1)
    for i in range(n-1):
        stairs[i+2] = stairs[i+1] + stairs[i]
    return stairs[n]