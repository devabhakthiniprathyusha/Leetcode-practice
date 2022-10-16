class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # sort - O(nlogn) with O(1)
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                print(nums[i])
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

