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
시간 복잡도: O(n^2)
- nums.index(pair) -> O(n)
- for loop 안에서 nums.index(pair) 최대 2번 호출 -> O(2n^2) -> O(n^2)

공간 복잡도: O(1)
- rs 배열에서 number 2개 저장 -> O(1) 공간
- nums 복사나 set/dict 없음
'''
