class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rs = []
        for i in range(len(nums) - 1, -1, -1):
            pair = target - nums[i]
            if pair not in nums or i == nums.index(pair):
                continue
            idx = nums.index(pair)
            if pair in nums:
                rs.append(i)
                rs.append(idx)
                break
        return rs        
        