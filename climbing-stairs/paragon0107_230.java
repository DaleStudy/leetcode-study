/*
*
* 시간 복잡도:
*   바텀업 형식으로 배열을 훑으며 올라가기 때문에 O(N)
* 공간 복잡도:
*   자연수 마다 해당하는 방법의 갯수를 저장하기 때문에 O(N)
*
* */
class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for(int i=3;i<=n;i++){
            dp[i] = dp[i - 2] + dp[i - 1];
        }
        return dp[n];
    }
}
