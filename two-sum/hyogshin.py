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

'''
시간 복잡도: for loop 사용 -> O(n) 
공간 복잡도: len(nums) + rs 배열에서 number 2개 저장
'''
