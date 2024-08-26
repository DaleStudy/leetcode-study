## Description

다이나믹 프로그래밍을 이용하여 풀 수 있습니다.

아래와 같이 `memo` 배열을 정의했을 때,

```
memo[0] = 1
memo[1] = 1
memo[i] = distinct ways to climb to the i-th stair
```

다음과 같은 점화식이 성립합니다.

```
memo[i] = memo[i - 2] + memo[i - 1] (i > 1)
```

## Big-O

Time complexity: O(N)

Space complexity: O(N)

---

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<int> memo(2, 1);

        for (int i = 2; i <= n; i++) {
            memo.push_back(memo[i - 1] + memo[i - 2]);
        }

        return memo[n];
    }
};
```
