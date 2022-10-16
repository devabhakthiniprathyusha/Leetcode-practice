class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # order maters
        # ace not for aec

        # using two pointers one from s and one from t
        # if present increment check count
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)