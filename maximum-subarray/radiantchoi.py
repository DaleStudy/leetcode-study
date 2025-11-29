class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # 원래라면 dp 배열을 만들어, i번째 원소까지 탐색한 결과 중 최댓값을 각각의 인덱스에 저장
        # 하지만 지금은 최댓값만 남기면 되므로 일차적 최적화
        current = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            result = max(result, current)

        return result
