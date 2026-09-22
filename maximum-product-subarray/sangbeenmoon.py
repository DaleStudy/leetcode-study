class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_val = nums[0]
        answer = max_val

        for i in range(1, len(nums)):
            target = nums[i]
            prev_max_val = max_val
            
            max_val = max(max_val * target, min_val * target, target)
            min_val = min(prev_max_val * target, min_val * target, target)
            answer = max(answer, max_val)

        return answer
            
                
