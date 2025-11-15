# 시간 복잡도
# 입력 list를 이중 for문에서 사용 -> O(n^2)
# 공간 복잡도
# 크기가 고정된 리스트 사용 -> O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for l in range(0, len(nums)):
                if i == l:
                    continue
                if nums[i] + nums[l] == target:
                    return [i, l]
