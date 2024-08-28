# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for idx, num in enumerate(nums):
            check[num] = idx

        for idx, num in enumerate(nums):
            # 동일한 숫자 두 개가 합쳐져서 목표값이 되는 경우
            if num * 2 == target:
                # 그리고 그 숫자가 리스트에 두 개 이상 존재할 경우
                if check[num] != idx:
                    return [idx, check[num]]
                continue

            if target - num in check:
                return [check[num], check[target - num]]

        return []
