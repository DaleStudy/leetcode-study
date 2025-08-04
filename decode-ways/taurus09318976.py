#계단 오르기 문제, 피보나치 수열과 동일한 패턴의 동적 프로그래밍 문제임
#차이점은 피보나치 수열은 0,1로 시작하며 나머지 두 문제는 1,1로 시작한다는 점
#디코딩 문제는 1)0이 아니어야 하며, 2)두 자리 숫자가 10~26 사이여야 한다는 조건이 주어진다는 점이 다름

class Solution:
    def numDecodings(self, s: str):
        #초기 예외값 처리. 빈 문자열이거나, 첫 문자가 0이면 디코딩 불가능
        if not s or s[0] == '0':
            return 0
        
        #DP 변수 초기화
        ##dp[i-2] 역할
        prev = 1  
        ##dp[i-1] 역할
        curr = 1  
        
        #DP 계산
        ##첫번째 인덱스부터 마지막까지
        for i in range(1, len(s)):  
            ##현재 위치의 디코딩 방법 수를 임시로 저장
            temp = 0  
            
            ##한 자리 숫자로 디코딩하는 경우
            ###현재 숫자가 0이 아니면
            if s[i] != '0': 
                ###이전 방법 수를 더함 
                temp += curr  
            
            ##두 자리 숫자로 디코딩하는 경우
            ###현재와 이전 숫자를 합친 두 자리 수가 10~26 사이면
            if 10 <= int(s[i-1:i+1]) <= 26:  
                ###두 자리 전 방법 수를 더함
                temp += prev  
            
            ##변수 업데이트
            ###이전 값을 두 자리 전 값으로 이동
            prev = curr  
            ###현재 값을 새로 계산된 값으로 이동
            curr = temp  
        
        #최종 디코딩 방법 수
        return curr  

# 테스트 케이스
solution = Solution()

# 테스트 1
test1 = "12"
print(f"Expected: 2")
print(f"Result: {solution.numDecodings(test1)}")

# 테스트 2
test2 = "226"
print(f"Expected: 3")
print(f"Result: {solution.numDecodings(test2)}")

# 테스트 3
test3 = "06"
print(f"Expected: 0")
print(f"Result: {solution.numDecodings(test3)}")


#시간 복잡도: O(n)
    #n = 입력 문자열 s의 길이
    #for 루프가 문자열의 길이만큼 한 번 실행됨
    #각 반복에서 수행하는 연산:
    #s[i] != '0' 비교: O(1)
    #int(s[i-1:i+1]) 변환: O(1)
    #10 <= two_digit <= 26 비교: O(1)
    #변수 업데이트: O(1)
    #따라서 전체 시간 복잡도는 O(n)
#공간 복잡도: O(1)
    #추가로 사용하는 공간:
    #prev: O(1)
    #curr: O(1)
    #temp: O(1)
    #i: O(1)
    #입력 크기 n과 무관하게 상수 개수의 변수만 사용
    #따라서 공간 복잡도는 O(1)

