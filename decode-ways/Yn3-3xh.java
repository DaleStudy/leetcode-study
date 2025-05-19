/**
[문제풀이]
- 만들 수 있는 가지수를 모두 구하기
- A ~ Z -> 1 ~ 26
- DP로 풀어보자.
time: O(N), space: O(N)
    1212를 예시로,
    첫번째 수를 가져올 때 dp[1] = 1
    만들어지는 수: 1
    
    한자리 수를 가져올 때 dp[2] = dp[1] = 1
    만들어지는 수: 1, 2
    두자리 수를 가져올 때 dp[2] = d[2] + dp[0] = 1 + 1 = 2
    만들어지는 수: 12
    >> 1, 2 | 12
    
    한자리 수를 가져올 때 dp[3] = dp[2] = 2
    만들어지는 수: 1, 2, 1 | 12, 1
    두자리 수를 가져올 때 dp[3] = dp[3] + dp[1] = 2 + 1 = 3
    만들어지는 수: 1, 21
    >> 1, 2, 1 | 12, 1 | 1, 21

    한자리 수를 가져올 때 dp[4] = dp[3] = 3
    만들어지는 수: 1, 2, 1, 2 | 12, 1, 2 | 1, 21, 2
    두자리 수를 가져올 때 dp[4] = dp[4] + dp[2] = 3 + 2 = 5
    만들어지는 수: 1, 2, 12 | 12, 2
    >> 1, 2, 1, 2 | 12, 1, 2 | 1, 21, 2 | 1, 2, 12 | 12, 2

[회고]
dfs로 풀려다가 잘 안풀어져서 DP로 노선을 틀었는데, 아직 DP 구현이 모자른 것 같다..

 */
class Solution {
    public int numDecodings(String s) {
        if (s.charAt(0) == '0') {
            return 0;
        }

        int len = s.length();
        int[] dp = new int[len + 1];
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= len; i++) {
            int one = Character.getNumericValue(s.charAt(i - 1));
            int two = Integer.parseInt(s.substring(i - 2, i));

            if (1 <= one && one <= 9) {
                dp[i] = dp[i - 1];
            }
            if (10 <= two && two <= 26) {
                dp[i] += dp[i - 2];
            }
        }
        return dp[len];
    }
}

