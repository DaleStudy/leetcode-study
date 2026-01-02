class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 자기 자신을 제외한 모든 인덱스의 곱을 곱하는 건, 자기 자신 기준 왼쪽 인덱스들의 곱과 오른쪽 인덱스들의 곱을 최종적으로 곱한 것과 동일하다.
        # answer[i]은 (i 기준 왼쪽 인덱스 값들의 누적 곱) * (i 기준 오른쪽 인덱스 값들의 누적 곱) 
        answers = [1 for _ in range(len(nums))]

        # 여기서 before_total_prod는 인덱스 i 기준 왼쪽 인덱스들의 누적 곱
        # 즉, before_total_prod = nums[1] * num[2] * ... * num[i - 2] * num[i - 1]
        before_total_prod = 1
        for i in range(1, len(nums)):
            before_total_prod *= nums[i - 1]
            answers[i] *= before_total_prod

        # 여기서 after_total_prod는 인덱스 i 기준 오른쪽 인덱스들의 누적 곱
        # 즉, after_total_prod = nums[n - 1] * num[n - 2] * ... * num[i + 2] * num[i + 1]
        # (n은 리스트 nums 의 길이, 구현은 n - 1 인덱스부터 거꾸로 계산)
        after_total_prod = 1
        for i in range(len(nums) - 2, -1, -1):
            after_total_prod *= nums[i + 1]
            answers[i] *= after_total_prod

        return answers
