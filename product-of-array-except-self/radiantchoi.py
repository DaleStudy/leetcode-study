class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        reduced = 1
        zeroes = 0

        for num in nums:
            if num != 0:
                reduced *= num
            else:
                zeroes += 1
        
        result = []

        for num in nums:
            if num == 0:
                result.append(0 if zeroes - 1 > 0 else reduced)
            else:
                result.append(0 if zeroes else reduced // num)
        
        return result
