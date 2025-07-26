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
        