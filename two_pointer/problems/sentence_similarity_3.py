class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        s1, s2 = sentence1.split(" "), sentence2.split(" ")
        n1, n2 = len(s1), len(s2)
        p1, p2 = 0, 0

        while p1 < n1 and p2 < n2 and s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1

        c1 = n1-1
        c2 = n2-1

        while c1 >= 0 and c1 >= p1 and c2 >= 0 and c2 >= p2 and s1[c1] == s2[c2]:
            c1 -= 1
            c2 -= 1

        if s1[0:p1] + s1[c1+1:n1] == s2 or s2[0:p2] + s2[c2+1:n2] == s1:
            return True

        return False

