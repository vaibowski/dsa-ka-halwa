def characterReplacement(s: str, k: int) -> int:
    left, best = 0, 0
    char_freq = {}
    for right in range(len(s)):
        char_freq[s[right]] = char_freq.get(s[right], 0) + 1
        window = right - left + 1
        if window - max(char_freq.values()) <= k:
            best = max(best, window)
        else:
            char_freq[s[left]] -= 1
            left += 1
    return best
