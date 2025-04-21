#이 문제는 피보나치 수열과 동일한 패턴을 가지고 있음. 피보나치 수열의 (n+1)번째 수와 같음

class Solution:
    def climbStairs(self, n: int) -> int:
        #n이 1이나 2인 경우는 바로 결과 반환
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        #첫 번째, 두 번째 계단의 방법 수 저장
        prev, curr = 1, 2
        
        #세 번째 계단부터 n계단까지 계산
        for i in range(3, n + 1):
            prev, curr = curr, prev + curr
        
        return curr


        #시간 복잡도: O(n)
            #for 루프가 n-2번 실행됨(3부터 n까지)
            #각 반복에서 상수 시간(1)의 연산만 수행됨
            #따라서 전체 시간은 n에 비례함
        
        #공간 복잡도: O(1)
            #추가적인 배열이나 리스트를 사용하지 않음
            #두 개의 변수(prev, curr)만 사용함
            #입력 크기(n)가 아무리 커져도 사용하는 공간은 일정함
