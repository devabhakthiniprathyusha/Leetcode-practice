# Time complexity: O(len(nums))
# Approach: Two pointer solution

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #if val ignore it, else replace it with same one
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l

