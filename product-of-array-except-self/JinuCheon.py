# 처음에 직관적으로 떠오른 O(n2) 풀이.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                result[j] *= nums[i]
        
        return result

# 고민하다가 LLM 에게 힌트 달라고 질문.
# 좌 / 우 누적곱으로 처리하는 방식.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(num)
        result = [1] * n
        
        # 왼쪽 누적곱을 result에 미리 채워둠
        cumulativeLeftSum = 1
        for i in range(n):
            result[i] = cumulativeLeftSum
            cumulativeLeftSum *= nums[i]
        
        # 오른쪽 누적곱을 곱해나가면서 완성
        cumulativeRightSum = 1
        for i in range(n - 1, -1, -1):
            result[i] *= cumulativeRightSum
            cumulativeRightSum *= nums[i]
        
        return result
