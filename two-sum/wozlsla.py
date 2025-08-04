class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idx를 따로 저장해두는 게 좋을까? X -> i를 사용하면 될듯
        # 만약, 거꾸로 계산한다면?

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
