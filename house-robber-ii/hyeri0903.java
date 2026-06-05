class Solution {
    public int rob(int[] nums) {
        /**
        1.문제: 인접한 집을 털지않고 훔칠 수 있는 최대 금액 반환
        2.constraints
        - nums.length min = 1, max= 100
        - value min = 0, max = 1000
        - 집들은 circle 형태, 인접한 집을 털면 alerting (0번째, 마지막 집 동시에 털 수 없음)
        3.solution
        - dp[i] = max(dp[i-1], dp[i-2] + nums[i]) -> 이전값 vs i 번째 털었을 경우 max 값
        - case는 2가지. 1)0집 포함, n-1불포함 2)0집 불포함, n-1 포함
         */
         int currentMax = 0;
         int n = nums.length;
         int[] dp = new int[n-1];
         int[] dp2 = new int[n];

         if(n == 1) return nums[0];
         if(n == 2) return Math.max(nums[0], nums[1]);

         dp[0] = nums[0];
         dp[1] = Math.max(dp[0], nums[1]);

        //case 1) 0번집 포함, N-1 불포함
         for(int i = 2; i < n-1; i++) {
            //i번째 털기 or i번째 안 털기
            dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]); 
         }

        dp2[0] = 0;
        dp2[1] = nums[1];
        //case 2) 0번집 불포함, N-1 포함
        for(int i = 2; i < n; i++) {
            //i번째 털기 or i번째 안 털기
            dp2[i] = Math.max(dp2[i-1], dp2[i-2] + nums[i]); 
        }
        int answer = Math.max(dp[n-2], dp2[n-1]);
        return answer;
    }
}
