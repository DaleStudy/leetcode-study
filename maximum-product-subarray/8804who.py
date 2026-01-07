class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)

        cumprod = 1
        cumprod_to_first_neg = 1
 
        for num in nums:
            if num == 0:
                cumprod = 1
                cumprod_to_first_neg = 1
            else:
                cumprod *= num
                if cumprod > 0:
                    answer = max(answer, cumprod)
                else:
                    answer = max(answer, cumprod//cumprod_to_first_neg)
                if cumprod_to_first_neg > 0:
                    cumprod_to_first_neg *= num
        return answer
    
