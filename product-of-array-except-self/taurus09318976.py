#이 문제는 배열의 각 요소 i를 제외한 나머지 요소들의 곱을 구하는 문제임
#1)각 요소 i를 기준으로 왼쪽 숫자들의 곱과 오른쪽 숫자들의 곱을 따로 계산, 2)최종 결과는 왼쪽 곱과 오른쪽 곱의 곱

class Solution:
    def productExceptSelf(self, nums: List[int]):
        #입력 배열의 길이를 저장
        ##Example 1의 경우 : len(nums) = 4
        n = len(nums)
        #결과를 저장할 배열을 곱셈의 항등원인 1로 모두 초기화
        #cf. 빈 집합의 곱은 1, 합은 0으로 정의됨
        ##answer = [1] * 4 = [1, 1, 1, 1]
        answer = [1] * n
        
        #i를 기준으로 왼쪽 숫자들의 곱을 계산
        #왼쪽 곱의 초기값
        left_product = 1
        for i in range(n):
            #현재 위치의 왼쪽 곱을 저장
            ##nums[0]의 왼쪽에는 아무 숫자도 없으므로, 
            ##아무것도 없는 상태의 곱은 1임. 따라서 answer[0]=1
            ##answer[1]=1 / answer[2]=2 / answer[3]=6      
            answer[i] = left_product
            #다음 위치를 위해 현재 수를 곱함
            ##left_product = 1 * 1 = 1 / left_product = 1 * 2 = 2
            ##left_product = 2 * 3 = 6 / left_product = 6 * 4 = 24
            left_product *= nums[i]
        
        ##첫 번째 for문 후 answer = [1, 1, 2, 6]
        #i를 기준으로 오른쪽 숫자들의 곱 계산 및 최종 결과 생성
        right_product = 1
        #오른쪽에서 왼쪽으로 순회
        for i in range(n-1, -1, -1):
            #현재 위치의 오른쪽 곱을 저장
            ##answer[3] = 6 * 1 = 6 / answer[2] = 2 * 1 = 2
            ##answer[1] = 1 * 1 = 1 / answer[1] = 1 * 1 = 1  
            answer[i] *= right_product
            #다음 위치를 위해 현재 수를 곱함
            ##right_product = 1 * 4 = 4 / right_product = 4 * 3 = 12
            ##right_product = 12 * 2 = 24 / right_product = 24 * 1 = 24
            right_product *= nums[i]
            
        
        #최종 결과를 반환
        ##최종 answer = [24, 12, 8, 6]
        return answer

        #시간 복잡도: O(n)
            ##두 번의 선형 순회만 수행하며, 각 순회는 O(n) 시간이 소요
        #공간 복잡도: O(1)
            ##추가적인 공간을 사용하지 않음
            ##단, 출력 배열은 문제의 요구사항이므로 제외




