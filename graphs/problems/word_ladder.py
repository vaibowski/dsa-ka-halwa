from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # return immediately if endWord is not in the wordList
        if endWord not in wordList:
            return 0

        # eliminate redundant words
        wordSet = set(wordList)
        length = len(beginWord)

        # make a pattern dict for each word by replacing 1 char each iteration, each word in wordlist will be added
        # against the pattern set as key. Time complexity = O(n*m) worst case
        # n being wordList size, and m being length of words
        patternDict = defaultdict(list)
        for word in wordSet:
            for i in range(length):
                patternDict[word[:i] + "*" + word[i + 1:]].append(word)

        # use BFS to search for the end word level by level
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            currentWord, steps = queue.popleft()
            for i in range(length):
                pattern = currentWord[:i] + "*" + currentWord[i + 1:]
                for word in patternDict[pattern]:
                    if word == endWord:
                        return steps + 1
                    if word not in visited:
                        queue.append((word, steps + 1))
                        visited.add(word)

        return 0
