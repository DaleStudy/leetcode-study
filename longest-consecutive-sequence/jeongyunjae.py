class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        result = [1] * len(nums)
        
        # 중복 제거 후 정렬
        nums = sorted(list(set(nums)))

        # 연속된 숫자 찾기
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                result[i] = result[i-1] + 1

        return max(result)
