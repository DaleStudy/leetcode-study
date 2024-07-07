- 문제: https://leetcode.com/problems/house-robber-ii/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/03/leetcode-213

## 내가 작성한 풀이

```java
public class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }

        if (nums.length == 3) {
            return Math.max(nums[2], Math.max(nums[0], nums[1]));
        }


        return Math.max(getMaxInRange(nums, 0, nums.length - 1), getMaxInRange(nums, 1, nums.length));
    }

    public int getMaxInRange(int[] nums, int start, int end) {
        int[] dp = new int[nums.length];
        int max;
        dp[start] = nums[start];
        dp[start + 1] = nums[start + 1];
        dp[start + 2] = nums[start + 2] + nums[start];
        max = Math.max(dp[start + 2], dp[start + 1]);
        for (int i = start + 3; i < end; i++) {
            dp[i] = Math.max(nums[i] + dp[i - 2], nums[i] + dp[i - 3]);
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
```

### TC, SC

시간 복잡도는 O(n), 공간 복잡도는 O(n) 이다.
