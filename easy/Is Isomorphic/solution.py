class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # create 2 hashmaps and check the characters
        # are not mapped to more than one character

        # return false false when mapped more than once in
        # any of the two hashmaps

        #O(n) and O(n)
        st, ts = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (((c1 in st) and (st[c1] != c2)) or
                    ((c2 in ts) and ts[c2] != c1)):
                return False

            st[c1] = c2
            ts[c2] = c1
        return True