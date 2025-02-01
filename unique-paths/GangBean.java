import java.math.BigDecimal;

class Solution {
    /**
    1. understanding
    - To reach destination, you have to move bottom direction in m-1 times, and move to right direction in n-1 times.
    - in example 2, [(DDR), (DRD), (RDD)] is the paths.
    - so, the number of paths are combinations of (m-1) D and (n-1) R
    - (m+n-2)!/(m-1)!(n-1)!, where ! means factorial, n! = 1*2*...*n
    - factorial[n]: n!
    2. complexity
    - time: O(m+n)
    - space: O(m+n)
     */
    public int uniquePaths(int m, int n) {
        BigDecimal[] dp = new BigDecimal[m+n];
        Arrays.fill(dp, BigDecimal.ONE);
        for (int num = 2; num < m+n; num++) {
            dp[num] = dp[num-1].multiply(new BigDecimal(num));
        }
        return dp[m+n-2].divide(dp[m-1]).divide(dp[n-1]).intValue();
    }
}

