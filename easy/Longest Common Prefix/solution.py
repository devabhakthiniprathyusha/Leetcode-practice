# Time complexity: O(S), where S is the sum of all characters in all strings.
# Approach: Vertical scanning with the length of minimum length.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n==1:
            return strs[0]
        mnLen = 201
        for x in strs:
            mnLen = min(mnLen, len(x))
        ans = ""
        for i in range(mnLen):
            ch = strs[0][i]
            for j in range(n):
                if strs[j][i] != ch:
                    return ans
            ans += ch
        return ans