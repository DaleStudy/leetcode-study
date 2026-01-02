class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        total = 0
        # subarray는 array에서 서로 인접해야함
        # 인접한 값의 합이 마이너스인 경우, 그냥 현재 값만 사용하는게 합보다 큼
        # total 이 0보다 작은경우 그냥 0으로 변경
        for num in nums:
            if total < 0:
                total = 0
            total += num
            max_total = max(total, max_total)
        # 시간복잡도 O(n), 공간복잡도 O(1)
        return max_total
