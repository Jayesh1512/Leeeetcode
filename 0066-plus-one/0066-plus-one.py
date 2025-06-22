class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        carry = 0
        digits[0] += 1
        for i in range(len(digits)):
            digits[i] += carry
            carry = digits[i] / 10
            digits[i] = digits[i] % 10
        if(carry == 1):
            digits.append(1)
        digits.reverse()
        return digits