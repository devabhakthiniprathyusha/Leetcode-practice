class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                print(nums[i])
                return True
        return False