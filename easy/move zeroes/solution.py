class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1

        if l != len(nums):
            for i in range(l, len(nums)):
                nums[i] = 0


