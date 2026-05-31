class Solution {
  /**
   * 인전합 두 집을 털면 안됨
   * 
   * i번째 집에서 할 수 있는 행위는? 2가지.
   * 털거나:
   * 털면 i-1번째 집은 안 털어야함, i-2번째 집은 털어도 괜찮겠지?
   * Money_A = nums[i] + DP[i-2]
   * 털지 않거나:
   * i번째 집을 안 털면, i-1번째집은 털어도 괜찮다.
   * Money_B = DP[i-1]
   * dp[i]를 i번째 집 앞에서 들고 있을 최대 금액이라고 할 때,
   * dp[i] = MAX(Money_A, Money_B)
   * 문제는 dp[nums.length-1]을 구하기
   */
  public int rob(int[] nums) {
    /**
     * 12분 소요.
     * Runtime: 0 ms (Beats 100%)
     * Memory: 42.74 MB (Beats 6.31%)
     * Space Complexity: O(N)
     * - nums 저장 => O(N)
     * - 최대 금액 저장 배열 => O(N)
     * > O(2N) ~= O(N)
     * Time Complexity: O(N)
     * - nums 처음부터 끝까지 조회하며 dp 저장. => O(N)
     * > O(N)
     */
    int[] dp = new int[nums.length];

    dp[0] = nums[0];
    if (nums.length > 1) {
      dp[1] = Integer.max(dp[0], nums[1]);
    }
    for (int i = 2; i < nums.length; i++) {
      // 터는 경우와 안터는 경우 중 최대 값.
      dp[i] = Integer.max(dp[i - 2] + nums[i], dp[i - 1]);
    }
    return dp[nums.length - 1];
  }
}
