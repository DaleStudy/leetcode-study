- https://leetcode.com/problems/reverse-bits/
- time complexity : O(1)
- space complexity : O(1)
- https://algorithm.jonghoonpark.com/2024/04/23/leetcode-190

```java
public class Solution {
    public int reverseBits(int n) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            ans <<= 1;
            ans |= (n & 1);
            n >>= 1;
        }
        return ans;
    }
}
```
