class Solution(object):
    def productExceptSelf(self, nums):
        """
        TimeComplexity: O(n)
        SpaceComplexity: O(n)
        """
        n = len(nums)
        

        # prefix product 수행
        # left는 i번째 요소 왼쪽에 있는 요소들의 곱
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # suffix product 수행
        # right는 i번째 요소 오른쪽에 있는 요소들의 곱
        right = [1] * n
        for i in range(n - 2, -1, -1): # 배열의 마지막 인덱스, [n - 1]은 이미 1로 초기화 되어 있으므로 
            right[i] = right[i + 1] * nums[i + 1]

        # 두 배열을 이용하여 최종 출력
        answer = [1] * n
        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer
