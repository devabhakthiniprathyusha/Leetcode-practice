class Solution:
    def added(self, n: int) -> int:
        addresult = 0
        while (n > 0):
            addresult += n % 10
            n = n // 10
            print(addresult)
        return addresult

    def addDigits(self, num: int) -> int:

        if num == 0:
            return 0
        while (num):
            print(num)
            if num > 9:
                num = self.added(num)
            else:
                return num
