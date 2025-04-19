#이 문제는 카데인 알고리즘(Kadane's Algorithm) 문제로 
#원래 배열에서 연속된 요소들로만 구성된 최대 부분 배열 합을 찾는 문제임

class Solution:
    def maxSubArray(self, nums: List[int]):
        #max_sum: 지금까지 발견한 가장 큰 부분 배열의 합
        #current_sum: 현재 고려 중인 부분 배열의 합  
        #위의 둘을 첫번째 요소로 초기화      
        max_sum = current_sum = nums[0] 
    
        #두 번째 요소부터 시작
        for num in nums[1:]:  
            #현재 숫자를 포함한 새로운 부분 배열의 합 계산
            current_sum = max(num, current_sum + num)
            #num: 현재 숫자만으로 새로운 부분 배열 시작
            #current_sum + num: 기존 부분 배열에 현재 숫자 추가
            
            #최대 합 업데이트
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# 테스트 케이스
solution = Solution()

# 테스트 1
test1 = [-2,1,-3,4,-1,2,1,-5,4]
print(f"Expected: 6")
print(f"Result: {solution.maxSubArray(test1)}")

# 테스트 2
test2 = [1]
print(f"Expected: 1")
print(f"Result: {solution.maxSubArray(test2)}")

# 테스트 3
test3 = [5,4,-1,7,8]
print(f"Expected: 23")
print(f"Result: {solution.maxSubArray(test3)}") 


#시간 복잡도: O(n)
    #n = nums의 길이
    #for 루프가 배열의 길이만큼 한 번 실행됨
    #각 반복에서 수행하는 연산:
    #max(num, current_sum + num): O(1)
    #max(max_sum, current_sum): O(1)
    #따라서 전체 시간 복잡도는 O(n)임
#공간 복잡도: O(1)
    #추가로 사용하는 공간:
    #max_sum: O(1)
    #current_sum: O(1)
    #num: O(1)
    #입력 크기 n과 무관하게 상수 개수의 변수만 사용
    #따라서 공간 복잡도는 O(1)임
