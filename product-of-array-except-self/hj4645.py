class Solution:
    # 정수 배열에 대해 answer 배열을 반환
    # 1. 정답 배열의 i번째 요소는 정수 배열의 i번째 요소를 제외한 다른 모든 요소의 곱
    # 2. 시간복잡도는 O(n) 이내로 해결 필요
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length  # 1로 초기화

        # 왼쪽 곱 계산 후 answer에 저장
        left = 1
        for i in range(length):
            answer[i] = left
            left *= nums[i]

        # 오른쪽 곱을 누적하면서 answer에 곱하기
        right = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

