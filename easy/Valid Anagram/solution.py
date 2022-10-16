class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs, ct = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            cs[s[i]] = 1 + cs.get(s[i], 0)  # if loop can be written in one line
            ct[t[i]] = 1 + ct.get(t[i],
                                  0)  # cs[s[i]] =1+cs.get(s[i],0)  if s[i] not present, then 0 or else add to count

        for c in cs:
            if cs[c] != ct.get(c, 0):
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT