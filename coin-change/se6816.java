/**
	내림차순 정렬 후, DFS를 통한 탐색 방식
	coins 길이 -> N
	amount 값 -> M
	시간 복잡도 : O(N^M) -> 시간 초과
	공간 복잡도 : O(M)
	
*/
class Solution2 {
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        for (int i = 0; i < coins.length / 2; i++) {
            int temp = coins[i];
            coins[i] = coins[coins.length-1-i];
            coins[coins.length-1-i] = temp;
        }
        return searchCoin(coins, 0, 0, amount, 0);
    }

    public int searchCoin(int[] coins, int idx, int result, int target, int count) {
        if(result == target) {
            return count;
        }
        int result2 = Integer.MAX_VALUE;
        for(int i = idx; i < coins.length; i++) {
            int temp = result + coins[i];
            if(temp > target) {
                continue;
            }
            int r = searchCoin(coins, i, temp, target, count+1);
            if(r != -1) {
                result2 = Math.min(result2, r);
            }
        }

        if(result2 == Integer.MAX_VALUE) {
            result2 = -1;
        }

        return result2;
    }
}

/**
	dp를 이용하여, 최저 값을 구하는 방식
	coins의 길이 -> N
	amount의 값 -> M
	시간 복잡도 : O(N*M)
	공간 복잡도 : O(M)
*/
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        
        for (int coin : coins) {
            for (int x = 0; x < amount; x++) {
                if(dp[x] == Integer.MAX_VALUE) {
                    continue;
                }
                if((x + coin) > amount) {
                    break;
                }

                dp[x + coin] = Math.min(dp[x + coin], dp[x] + 1);

            }
        }

        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }

}
