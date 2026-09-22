class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        i = 0
        arr = [0] * len(nums)
        while i <= max_jump:
            num = nums[i]
            for j in range(min(num + i, len(nums) - 1), i - 1, -1):
                if arr[j] == 1:
                    break
                arr[j] = 1
                max_jump = max(max_jump, j)

            i += 1

        return len(nums) - 1 == max_jump
