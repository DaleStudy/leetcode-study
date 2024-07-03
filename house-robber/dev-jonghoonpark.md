- 문제: https://leetcode.com/problems/house-robber/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/03/leetcode-198

## 내가 작성한 풀이

```java
public class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length];
        int max = 0;

        if (nums.length == 1) {
            return nums[0];
        }

        if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }

        if (nums.length == 3) {
            return Math.max(nums[2] + nums[0], nums[1]);
        }

        dp[0] = nums[0];
        dp[1] = nums[1];
        dp[2] = nums[2] + nums[0];
        max = Math.max(dp[2], dp[1]);
        for (int i = 3; i < nums.length; i++) {
            dp[i] = Math.max(nums[i] + dp[i - 2], nums[i] + dp[i - 3]);
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
```

### TC, SC

시간 복잡도는 O(n), 공간 복잡도는 O(n) 이다.
