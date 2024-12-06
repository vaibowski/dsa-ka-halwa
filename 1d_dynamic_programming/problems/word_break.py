from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False] * len(s)

    for i in range(len(s)):
        for w in wordDict:
            if w == s[i-len(w)+1 : i+1] and (dp[i-len(w)] or i-len(w) == -1):
                dp[i] = True

    return dp[-1]