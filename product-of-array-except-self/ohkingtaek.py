class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        처음에 모두 곱한걸 나눈다고 생각했으나, 0을 나누기 힘들고 다른 방식으로 답이 있을거라 생각함.
        각 요소에 대해 자신을 제외한 나머지 요소들의 곱을 계산.
        왼쪽에서부터 곱을 계산하여 answer[i]에 저장하고, 오른쪽에서부터 곱을 계산하여 answer[i]에 곱함.
        시간복잡도 O(n), 배열을 두 번 순회하여 결과를 계산.
        """
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
