class Solution {
  /**
   * 계산 n개를 오르기 위해 1 또는 2개씩 오르는 모든 경우의 수를 구하기
   * 
   * DP문제 풀이 과정
   * 1. 문제 단순화
   * - 숫자 N을 만들기 위해 1 또는 2를 더하는 순서를 만드는 경우의 수
   * 2. 문제에서 원하는 것
   * - N을 만들기 위한 모든 경우의 수
   * => DP[N] = N을 만들기 위한 모든 경우의 수
   * 2. 규칙 찾기
   * - N은 N-1에서 1 더하거나, N-2에서 2를 더하면 도달할 수 있다.
   * - 따라서 N에 도달하기 위한 경우의 수는 N-1을 도달하기 위한 경우의 수 + N-2에 도달하기 위한 경우의 수
   * - DP[0] = 1 => 움직이지 않는다는 경우의 수
   * - DP[1] = 1 => 1칸 움직이는 경우의 수
   * - DP[N] = DP[N-2] + DP[N-1]
   */
  public int climbStairs(int n) {
    /**
     * Runtime: 0 ms (Beats 100.00%)
     * Memory: 42.00 MB (Beats 15.00%)
     * Space Complexity: O(N)
     * - N 크기의 배열 1개 사용으로 O(N)
     * > O(N)
     * Time Complexity: O(N)
     * - N회 덧셈으로 => O(N)
     * > O(N)
     */
    int[] dp = new int[n + 1];
    dp[0] = 1;
    dp[1] = 1;

    for (int i = 2; i < n + 1; i++) {
      dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
  }
}
