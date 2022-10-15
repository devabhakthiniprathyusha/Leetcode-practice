# Time complexity: O(len(nums))
# Approach: Two pointer solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #using two index method to find unique elements and replace the values using r pointer
        l = 1

        for r in range(1, len(nums)):
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1

        return l

