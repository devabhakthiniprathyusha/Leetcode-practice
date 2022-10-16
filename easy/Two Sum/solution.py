# Time complexity: O(nlogn)
# Approach: iterate through the list keeping the track of available elements and their indices in dict.
# When the complementry item arrives, return the indices.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(nums):
            # 0, nums[0]
            # 1, nums[1]
            for i + 1 in range(nums):
                if nums[i] + nums[i + 1] == target:
                    output.append(i)
                    output.append(i + 1)
        return output

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, v in enumerate(nums):
            diff = target - v

            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[v] = i
