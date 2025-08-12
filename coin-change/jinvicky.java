import java.util.Arrays;

class Solution {
    public int coinChange(int[] coins, int amount) {
        int max=amount+1;
        int [] dp=new int[amount+1];
        Arrays.fill(dp,max);
        dp[0]=0;
        for(int coin:coins){
            for(int j=coin;j<=amount;j++){ // coin부터 시작해서 일반 루프보다 성능 향상
                dp[j]=Math.min(dp[j],dp[j-coin]+1);
            }
        }
        return dp[amount]>amount ? -1:dp[amount];
    }
}