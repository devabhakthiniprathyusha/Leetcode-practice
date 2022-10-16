# Time complexity: O(nlog(n)) where n is length of string in strs
# Approach: Sort all strings and group them

class Solution:
    # using sorted O(m*n*logn) m-lenght of strs and n is len of string in strs
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    # using hash O(m*n*26) = O(mn)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        mp = {}
        tmp = strs.copy()
        for i in range(n):
            tmp[i] = ''.join(sorted(tmp[i]))
        for i in range(n):
            if tmp[i] in mp:
                mp[tmp[i]].append(strs[i])
            else:
                mp[tmp[i]] = [strs[i]]
        ans = []
        for k, v in mp.items():
            ans.append(v)
        return ans