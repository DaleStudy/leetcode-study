public class Geegong {

    /**
     * time complexity : O(N)
     * space complexity : O(N)
     * @param n
     * @return
     */
    public int climbStairs(int n) {
        // 계단 n step 까지의 방법의 수는 f(n-1) + f(n-2)
        // f(n-1) 은 한칸 전 , f(n-2)는 2칸 전
        int[] dp = new int[46];
        dp[1] = 1;
        dp[2] = 2;


        for(int index=3; index<n; index++) {
            // (dp[index-1] + 한칸 더)의 방법의 수 + (dp[index-2] + 두칸 더)의 방법의 수
            dp[index] = dp[index-1] + dp[index-2];
        }

        return dp[n];
    }

}
