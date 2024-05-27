- https://leetcode.com/problems/counting-bits/
- time complexity : O(n \* log n), logn 이 붙는 이유는 bit는 log를 따라 수가 결정되기 때문
- space complexity : O(n)
- https://algorithm.jonghoonpark.com/2024/04/23/leetcode-338

```java
public int[] countBits(int n) {
    int result[] = new int[n + 1];
    for (int i = 0; i <= n; i++) {
        int num = i;
        int count = 0;
        while (num > 0) {
            count += num & 1;
            num = num >> 1;
        }
        result[i] = count;
    }
    return result;
}
```
