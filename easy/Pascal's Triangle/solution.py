# Time complexity: O(n*n)
# Approach: Pascal triangle can be constructed using the last row of the triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # adding zero one in front and one in end
        # basically add the two number and create a new list nd append to res
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res

    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, i):
                ab, cd = ans[i-1][j], ans[i-1][j-1]
                tmp.append(ab+cd)
            tmp.append(1)
            ans.append(tmp)
        return ans