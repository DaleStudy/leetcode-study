class Solution:
    def twoSum(self, target: int, nums: List[int], starting: int) -> List[List[int]]:
        left = starting
        right = len(nums) - 1

        result = []

        while left < right:
            if nums[left] + nums[right] == target:
                result.append([nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        
        return result
    
    def kSum(self, n: int, target: int, nums: List[int], starting: int) -> List[List[int]]:
        if n < 2 or starting == len(nums):
            return []
        elif n == 2:
            return self.twoSum(target, nums, starting)
        
        result = []

        for i in range(starting, len(nums) - n + 1):
            if i > starting and nums[i] == nums[i - 1]:
                continue
            
            for tail in self.kSum(n - 1, target - nums[i], nums, i + 1):
                result.append([nums[i]] + tail)
        
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.kSum(3, 0, nums, 0)
