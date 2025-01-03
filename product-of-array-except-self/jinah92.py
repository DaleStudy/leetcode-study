# O(n) time, O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_product = math.prod(filter(lambda x: x != 0, nums))
        raw_product = math.prod(nums)
        zero_total = nums.count(0)

        result = []

        for num in nums:
            if zero_total > 1:
                result.append(0)
            elif zero_total == 1:
                if num == 0:
                    result.append(non_zero_product)
                else:
                    result.append(raw_product)
            else:
                result.append(raw_product // num)
        
        return result
