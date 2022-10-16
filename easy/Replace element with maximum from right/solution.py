class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # starting from end of loop
        # initialise the last element with -1
        # calculate the maximum of 2 elements and replace with maximum of 2
        # instead of looping again and again

        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr