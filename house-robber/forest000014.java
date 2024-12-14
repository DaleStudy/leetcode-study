class Solution {
    /*
        [1, i]의 범위에서 최대값을 구하고자 할 때, 만약 [1, i-1]의 범위에서의 최대값을 이미 계산해 놓았다면 O(1)에 계산할 수 있다는 아이디어에서 출발합니다.
        단, 연속해서 두 집에서 훔칠 수 없다는 전제조건이 있으므로, i-1번째 집에서 훔친 경우와 훔치지 않는 경우 각각에 대한 최대값을 따로 구해두어야 합니다.
        dp[i-1][0]에는 i-1번째 집에서 훔치지 않는 경우의 최대값, dp[i-1][1]에는 i-1번째 집에서 훔친 경우의 최대값이 저장되어 있다는 전제하에,
        dp[i][0], dp[i][1]을 아래와 같이 구할 수 있습니다.

        1) i번째 집에서 훔치지 않는 경우의 [1, i] 범위에서의 최대값
        i번째 집에서는 훔치지 않을 것이므로, [1, i-1] 범위에서의 최대값이 dp[i][0]이 됩니다.
        단, 여기서 주의할 점은 dp[i-1][1]이 무조건 dp[i-1][0] 이상이라고 착각할 수 있다는 건데요,
        {100, 1, 1, 100} 에서 dp[1][0] = 100, dp[1][1] = 1 이라는 케이스를 생각해보면, dp[i-1][0], dp[i-1][1]를 비교해서 큰 것을 선택해야 함을 알 수 있습니다.

        2) i번째 집에서 훔치는 경우의 [1, i] 범위에서의 최대값
        i번째 집에서 훔치기 위해서는, i-1번째 집에서는 훔치지 않았어야만 합니다.
        따라서 단순히 dp[i][1] = dp[i-1][0] + nums[i] 가 됩니다.

        Runtime: 0 ms(Beats: 100.00 %)
        Time Complexity: O(n)
        - nums iteration : O(n)

        Memory: 41.04 MB(Beats: 43.05 %)
        Space Complexity: O(n)
        - dp[n][2] : O(n) * 2 = O(n)
    */
    public int rob(int[] nums) {
        int[][] dp = new int[nums.length][2];

        dp[0][1] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = dp[i - 1][0] + nums[i];
        }

        return Math.max(dp[nums.length - 1][0], dp[nums.length - 1][1]);
    }

    /*
        생각해보니 memoization 배열을 굳이 들고다닐 필요가 없어서,
        필요한 값(직전 인덱스에서의 memoization 값)만 저장하도록 수정해서 공간 복잡도를 개선했습니다.
        그런데... 무슨 이유에선지 오히려 메모리 사용량은 더 증가했다고 나오네요...?

        Runtime: 0 ms(Beats: 100.00 %)
        Time Complexity: O(n)
        - nums iteration : O(n)

        Memory: 41.21 MB(Beats: 22.01 %)
        Space Complexity: O(1)
    */
    public int rob2(int[] nums) {
        int[] dp = new int[2];

        dp[1] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int tmp0 = Math.max(dp[0], dp[1]);
            int tmp1 = dp[0] + nums[i];
            dp[0] = tmp0;
            dp[1] = tmp1;
        }

        return Math.max(dp[0], dp[1]);
    }
}
