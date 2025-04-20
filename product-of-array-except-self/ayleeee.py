# 정수 배열 nums가 주어졌을 때, 각 위치 i에 대해
# nums[i]를 제외한 나머지 모든 요소의 곱을 반환하는 함수를 작성

'''
nums = [1, 2, 3, 4]
answers = [24, 12, 8, 6]
answers[0] = 2 * 3 * 4 
answers[1] = 1 * 3 * 4
answers[2] = 1 * 2 * 4
answers[3] = 1 * 2 * 3

조건 : O(n) 시간 복잡도

왼쪽에서 오른쪽으로 누적 곱 계산
오른쪽에서 왼쪽으로 순회하면서, 오른쪽 누적 곱을 계산
왼쪽 누적 곱과 곱하여 최종 결과 업데이트 

'''
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    left = 1
    right = 1
    # 왼쪽에서 오른쪽으로 누적 곱 계산
    for i in range(n):
        result[i] = left
        left *= nums[i]
    # 오른쪽에서 왼쪽으로 누적 곱 계산  
    # 역순으로 반복하는 구문, 오른쪽에서 왼쪽으로 순회
    # range(start, stop, step) => 반복을 시작할 값, 반복을 멈출 값, 반복의 증가 또는 감소 단위
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]    
    return result
