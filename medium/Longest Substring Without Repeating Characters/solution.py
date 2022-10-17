# Time complexity: O(n)
# Approach: Window based mapping of characters and tracking of max length.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        mp = {}
        i, j, mx = 0, 0, 0
        while i < len(s) and j < len(s):
            mp[s[i]] = 1 if s[i] not in mp else mp[s[i]]+1
            if len(mp) == i-j+1:
                mx = max(mx, i-j+1)
            else:
                while len(mp) < i-j+1:
                    mp[s[j]] -= 1
                    if mp[s[j]] == 0:
                        del mp[s[j]]
                    j+=1
            i+=1
        return mx

    class Solution:
        # O(2n) space- O(min(m,n))
        def lengthOfLongestSubstring(self, s: str) -> int:
            chars = Counter()

            left = right = 0

            res = 0
            while right < len(s):
                r = s[right]
                chars[r] += 1

                while chars[r] > 1:
                    l = s[left]
                    chars[l] -= 1
                    left += 1

                res = max(res, right - left + 1)

                right += 1
            return res

        # O(n) space- O(min(m,n))
        def lengthOfLongestSubstring(self, s: str) -> int:
            n = len(s)
            ans = 0
            # mp stores the current index of a character
            mp = {}

            i = 0
            # try to extend the range [i, j]
            for j in range(n):
                if s[j] in mp:
                    i = max(mp[s[j]], i)

                ans = max(ans, j - i + 1)
                mp[s[j]] = j + 1

            return ans

