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


# 7기 풀이
# 시간 복잡도: O(n)
#  - nums의 길이만큼이 최대 연산 횟수가 된다. for문 두 번 돌린 것은 O(2n) -> O(n)으로 표기 가능
# 공간 복잡도: O(n)
#  - nums의 길이만큼 res를 만든다.
#  - 단 이는 return variable이라서 리트코드에서는 공간 복잡도 계산에서 제외, 조건의 O(1)와 동일하다고 할 수 있다.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 정답에 대한 리스트 추가
        res = [1 for _ in range(len(nums))]

        previous_res = 1
        for i in range(len(nums)):
            # i번째 인덱싀 이전까지의 값들을 res[i]에 먼저 곱해준 후,
            # 자기 자신을 previous_res에 계산한다. 이는 다음 loop, 즉 i+1번째일 때 계산된 값을 그대로 곱하게 된다.
            res[i] *= previous_res
            previous_res *= nums[i]

        next_res = 1
        for i in range(len(nums) -1, -1, -1):
            # 리스트의 맨 뒷쪽 index부터 계산해주면 i번째 인덱스 이후의 값들의 곱들을 계산할 수 있다.
            # i번째 인덱싀 이후까지의 값들을 res[i]에 먼저 곱해준 후,
            # 자기 자신을 next_res 계산한다. 이는 다음 loop, 즉 i-1번째일 때 계산된 값을 그대로 곱하게 된다.
            res[i] *= next_res
            next_res *= nums[i]

        return res
