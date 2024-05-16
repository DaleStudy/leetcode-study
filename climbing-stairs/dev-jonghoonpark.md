- https://leetcode.com/problems/climbing-stairs
- time complexity : O(n)
- space complexity : O(1)
- https://algorithm.jonghoonpark.com/2024/02/09/leetcode-70

```java
class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        }

        int result = 0;
        int temp1 = 1, temp2 = 2;
        for(int i = 3; i <= n; i++) {
            result = temp1 + temp2;
            temp1 = temp2;
            temp2 = result;
        }

        return result;
    }
}
```
