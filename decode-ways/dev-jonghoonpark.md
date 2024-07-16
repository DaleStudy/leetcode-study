- 문제: https://leetcode.com/problems/decode-ways/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/08/leetcode-91

```java
class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length()];

        if (s.charAt(0) == '0') {
            return 0;
        }
        dp[0] = 1;

        for (int i = 1; i < s.length(); i++) {
            int oneDigit = Integer.parseInt(String.valueOf(s.charAt(i)));
            if (oneDigit > 0) {
                dp[i] = dp[i - 1];
            }

            int prevDigit = Integer.parseInt(String.valueOf(s.charAt(i - 1)));
            if (prevDigit == 0) {
                continue;
            }

            int twoDigit = prevDigit * 10 + oneDigit;
            if (twoDigit <= 26) {
                if (i > 2) {
                    dp[i] = dp[i] + dp[i - 2];
                } else {
                    dp[i] = dp[i] + 1;
                }
            }
        }

        return dp[s.length() - 1];
    }
}
```

### TC, SC

시간 복잡도는 O(n), 공간 복잡도는 O(n)이다.
이런식으로 최근 데이터만 재사용 하는 경우에는 공간복잡도를 O(1) 으로도 줄일 수 있을 것이다.
최근의 데이터가 아닌 이전 데이터들은 더 이상 참조되지 않기 때문에 필요한 공간만 만들어서 보관하면 된다.
