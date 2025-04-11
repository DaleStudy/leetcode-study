class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        f(n)이 계단을 올라갈 수 있는 방법의 수라면,
        f(n) = f(n-1) + f(n-2)
        - Time Complexity
          재귀로 푸는 경우 지수 시간이 소요되지만,
          아래와 같이 다이나믹 프로그래밍으로 푸는 경우
          O(n) 소요 됨
        - Space Complexity
          재귀로 푸는 경우, 재귀 호출 스택이 O(n)만큼의 공간을 사용할 수 있음
          아래와 같이 다이나믹 프로그래밍으로 푸는 경우,
          리스트 dp에 각 인덱스 별로 결과를 저장하므로 O(n) 사용 됨

        """
    
        # n이 1인 경우 방법은 하나뿐
        if n == 1:
            return 1
        
        # 길이가 n+1인 리스트 생성
        # 인덱스 0: 시작점(0번째)
        # 인덱스 n: n번째 계단
        dp = [0 for i in range(n + 1)] 

        dp[1] = 1 # n = 1이면 1을 반환
        dp[2] = 2 # n = 2이면 2를 반환

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
