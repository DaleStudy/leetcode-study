/**
 * 정수 배열 coins가 주어졌을 때 amount를 만들 기 위해 최소한의 동전 개수를 반환하세요.
 만약 동적으로 amount 조합을 만들어낼 수 없다면 -1을 리턴하세요.
 */
import java.util.Arrays;

class Solution {

    // 시간복잡도: O(n * amount), 공간복잡도: O(amount)
    public int coinChange(int[] coins, int amount) {
        int[] coinCnt = new int[amount + 1];
        // coins[i]의 최댓값이 2^31 - 1 이므로 최댓값 설정
        Arrays.fill(coinCnt, Integer.MAX_VALUE - 1);
        coinCnt[0] = 0;
        for (int i = 0; i < coins.length; i++) {
            for (int j = coins[i]; j < amount + 1; j++) {
                coinCnt[j] = Math.min(coinCnt[j], coinCnt[j - coins[i]] + 1);
            }
        }
        if (coinCnt[amount] == Integer.MAX_VALUE - 1) {
            return -1;
        }
        return coinCnt[amount];
    }
}

