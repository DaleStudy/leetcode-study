class Solution(object):
    def productExceptSelf(self, nums):
        """
        TimeComplexity: O(n)
        SpaceComplexity: O(1)
        """
        n = len(nums)
        answer = [1] * n # 결과를 저장하는 리스트
        
        # i번째 요소 왼쪽에 있는 요소들에 대해 prefix product 수행
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # 오른쪽에 있는 요소들에 대해 suffix product 수행
        right = 1 # 오른쪽 누적 곱
        for i in range(n - 1, -1, -1): 
            answer[i] *= right # 현재 인덱스 왼쪽 곱과 오른쪽 곱을 곱함
            right *= nums[i] #오른쪽 누적 곱 업데이트

        return answer
