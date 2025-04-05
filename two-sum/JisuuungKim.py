class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            cur = nums[i]
            x = target - cur
            if x in d:
                return [i, d[x]]
            else:
                d[cur] = i

    # 시간복잡도 O(n)
