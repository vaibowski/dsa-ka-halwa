from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())