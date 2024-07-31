- 문제: https://leetcode.com/problems/sum-of-two-integers/
- 풀이: https://algorithm.jonghoonpark.com/2024/01/31/leetcode-371

```java
class Solution {
  public int getSum(int a, int b) {
    while (b != 0) {
      int _a = (a ^ b);
      int _b = ((a & b) << 1);
      a = _a;
      b = _b;
    }

    return a;
  }
}
```

### TC, SC

시간 복잡도는 O(1), 공간복잡도는 O(1) 이다. 최악의 경우 b의 비트수(32)만큼 반복문이 진행된다.
