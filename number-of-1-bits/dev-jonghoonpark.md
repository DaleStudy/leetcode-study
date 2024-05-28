- https://leetcode.com/problems/number-of-1-bits/
- time complexity : O(logn)
- space complexity : O(1)
- https://algorithm.jonghoonpark.com/2024/02/20/leetcode-191

```java
public int hammingWeight(int n) {
    int count = 0;
    while (n != 0) {
        count += n % 2;
        n = n >> 1;
    }
    return count;
}
```
