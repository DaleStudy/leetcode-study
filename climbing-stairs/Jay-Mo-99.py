        #해석
        #피보나치 수열을 이용하여 특정 범위마다 1과 2를 활용한 방법의 수를 계산한다. 
        #a=1, a=2 로 초기 셋팅 후 반복문마다 a와 b를 업데이트 한다. 
        # a는 현재 계단의 경우의 수, b는 다음 계단의 경우의 수로 설정한다. 
        # 반복문의 결과로 n번째 계단을 오르는 방법의 수(a)를 반환한다.


        #Big O
        #N: 매개변수 n의 크기(계단 갯수)
        
        #Time Complexity: O(N)
        #- for loop 는 n-1번 : O(N)
        
        #Space Complexity: O(1)
        #- 상수 a,b만 사용 : O(1)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b = 1,2 #F(0) = 1, F(1) =2
        for i in range(1,n):
            a,b = b, a+b #Update a and b each iteration
            #Fn = Fn-1 + Fn-2

        return a
        
