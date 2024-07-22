- 문제: https://leetcode.com/problems/maximum-subarray/
- 풀이: https://algorithm.jonghoonpark.com/2024/05/07/leetcode-53

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE;
        int currentSum = 0;

        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            maxSum = Math.max(maxSum, currentSum);
            currentSum = Math.max(currentSum, 0);
        }

        return maxSum;
    }
}
```

- currentSum이 maxSum보다 클 경우 maxSum을 갱신한다.
- currentSum은 음수일 경우 (0보다 작을 경우) 0으로 초기화 한다.

### TC, SC

시간 복잡도는 O(n), 공간 복잡도는 O(1) 이다.
