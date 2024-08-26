## Description

DP를 이용하여 풀이할 수 있습니다.

배열 `memo`를 아래와 같이 정의합니다.

```
memo[i] = i원을 만들기 위해 필요한 동전의 최소 개수
각 원소의 값은 초기값은 10^4 + 1로 설정함 (max(amount) / min(coin) + 1)
```

앞서 정의한 배열 `memo`를 이용하면 아래 점화식이 성립합니다.

```
memo[i] = min(memo[i], memo[i - coin] + 1) if i - coin >= 0
```

## Big-O

배열 `coins`의 크기를 `N`, 정수 `amount`의 크기를 `K`라고 했을 때,

Time complexity: `O(N * M)`

Space complexity: `O(M)`

---

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int MAX = 10000 + 1;
        vector<int> memo(amount + 1, MAX);
        memo[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (auto coin : coins) {
                if (i - coin >= 0) {
                    memo[i] = min(memo[i], memo[i - coin] + 1);
                }
            }
        }

        return memo[amount] == MAX ? -1 : memo[amount];
    }
};
```
