class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = digits[-1] + 1
        digits[-1] = temp%10
        carry = int(temp/10)
        for i in range(len(digits)-2,-1,-1):
            temp = digits[i] + carry
            digits[i] = temp%10
            carry = int(temp/10)
        answer = digits
        if carry:
            answer = [carry] + digits
        return answer