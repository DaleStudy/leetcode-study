class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        nums = sorted(list(s))
        rs = []
        cnt = 1

        for i in range(len(nums)-1):
            if (nums[i] + 1) == nums[i+1]:
                cnt += 1
            else:
                rs.append(cnt)
                cnt = 1

        rs.append(cnt)
        return max(rs)
        
'''
시간 복잡도: for loop 1회 -> O(n)
공간 복잡도: nums 리스트 + rs 배열 (최대 len(nums)) + sorted로 nums 배열 복사 
'''
