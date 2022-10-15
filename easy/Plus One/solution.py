# Time complexity: O(n)
# Approach: Adding carry till it reaches the most significant digit and then if it still remains, then create new array and extend.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if the last digit is 9, carry forward and make carry 0
        # inserting at first is two complicated so reverse the list in first
        digits = digits[::-1]
        carry, i = 1, 0
        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1
        return digits[::-1]
