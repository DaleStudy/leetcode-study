import java.util.Arrays;


// 왜 greedy가 아닐까? amount가 7이라고 가정했을 때 greedy라면 [1,3,4,5]에서 5를 우선시해서 5+1+1 총 3개를 사용할 것이지만,
// 실제 정답은 3+4 로 총 2개가 된다. 그렇기에 단순히 욕심쟁이로 최댓값, 최솟값으로 접근하는 방식은 적합하지 않다.
// greedy가 아니라면 보통 DP로 풀이한다.
// DP의 기초인 1. Climbing Stairs 2. Best Time to Buy and Sell Stock 3. House Robber를 선행으로 풀고 접근했다.
// DP의 기본은 i-1, i-2식으로 기존 값을 재사용하는 메모이제이션인데 나는 bottom-up으로 모든 dp를 풀이하려고 노력한다. (일관성)
// DP는 값을 비교하기 위해서 Math.min(), Math.max()를 많이 사용하기에 초기값을 Integer.MAX_VALUE, Integer.MIN_VALUE로 염두했다.

class Solution {
    public int coinChange(int[] coins, int amount) {
        int max = amount + 1; // 값 미표현이라면 Integer.MAX_VALUE가 더 직관적이지 않나? -> testcase에서 음수값 나와서 실패함
        int[] dp = new int[amount + 1]; // 목표인 amount를 위한 공간 확보를 위해서 amount+1로 배열 사이즈를 측정
        Arrays.fill(dp, max); // 최소 개수를 구하는 것이기 때문에 max값으로 채웠다.
        dp[0] = 0; // 첫 요소만 max가 아닌 0으로 설정한다. ->
        // 그냥 0부터 amount까지 이중 for문 하는 것보다
        // j문에서 바깥 i의 코인값부터 인덱스로 시작하는 것이 같은 결과, 높은 성능.
        for (int coin : coins) {
            for (int j = coin; j <= amount; j++) {
                // dp[j - coin]: coin 동전을 하나 사용했을 때, 남은 금액 j - coin을 만드는 최소 동전 개수
                // 코인값을 인덱스로서 계산해야 한다는 것을 몰랐음 j-coin에서 한참을 헤맨....
                dp[j] = Math.min(dp[j], dp[j - coin] + 1);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
