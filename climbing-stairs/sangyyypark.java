/**
 1. 문제 이해
 N이 주어지면 1부터 N까지의 숫자를 이용해서 N까지 도달 가능한 경우의 수(+1,+2만 가능)를 반환해야 하는 문제임. 중복을 허용하는 순열을 찾는 문제이다.

 2. naive algorithm 도출
 피보나치 수열임.
 N=1일때 가능한 경우의 수는 1
 N=2일때 가능한 경우의 수는 2
 N=3일때 가능한 경우의 수는 3 (n-2번째와 n-1번째의 합)

 3. 시간복잡도 분석

 O(N)
 4. 코드작성
 */
class sangyyypark {
    public int climbStairs(int n) {
        if(n ==1) return 1;
        if(n==2) return 2;
        int [] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        for(int i = 3; i <= n; i++) {
            dp[i] = dp[i-2] + dp[i-1];
        }
        return dp[n];
    }
}

