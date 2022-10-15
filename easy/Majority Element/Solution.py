class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        maximum = 0
        for a in nums:
            if a not in d:
                d[a] = nums.count(a)
                if d[a] >= maximum:
                    maximum = d[a]
                    result = a
        return result

    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        return max(d.keys(), key=d.get)
