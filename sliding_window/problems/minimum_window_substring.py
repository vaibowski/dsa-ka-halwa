def minWindow(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    cache = {}
    l, r, l_idx, count, best = 0, 0, 0, len(t), float('inf')
    # trick is to use a count variable to increase the frequency stored in cache for char in t
    # when we move the left boundary of our minimum window

    for ch in t:
        cache[ch] = cache.get(ch, 0) + 1

    while r < len(s):
        if cache.get(s[r], 0) > 0:
            count -= 1
        cache[s[r]] = cache.get(s[r], 0) - 1
        r += 1

        while count == 0:
            if r - l < best:
                l_idx = l
                best = r - l

            if cache.get(s[l], 0) == 0:
                count += 1
            cache[s[l]] = cache.get(s[l], 0) + 1
            l += 1

    return "" if best == float('inf') else s[l_idx: l_idx + best]
