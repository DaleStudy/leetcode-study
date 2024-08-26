## Description

`queue`를 이용한 BFS로 주어진 `candidates`의 조합을 만듭니다.

조합의 합 S의 크기에 따라 아래와 같이 연산을 진행합니다.

```
S < target: 조합에 새로운 수를 추가하여 queue에 다시 push
S == target: 정답 배열 res에 해당 조합을 push
S > target: 더 이상 queue에 조합을 등록하지 않음
```

## Big-O

`candidates` 배열의 크기를 `N`, `target`의 크기를 `T`, `candidates` 배열의 원소 중 가장 작은 원소의 크기를 `K`라고 했을 때,

Time complexity: `O(N ^ (T / K))`

- `queue`에 담긴 각 조합들은 최대 `N`개의 새로운 조합들을 만들어 낼 수 있습니다
- 이걸 `Tree`에 빗대어 생각해보면 각 `node` 당 `N`개의 자식들을 갖는다고 볼 수 있습니다
- `Tree`의 깊이는 `T / K`에 비례합니다

Space complexity: `O((T / K) * (N ^ (T / K)))`

- `queue`의 크기는 앞서 말한 `Tree`의 `node` 개수만큼 늘어날 수 있습니다
- `node`가 지닌 조합 배열의 크기는 `T / K` 까지 커질 수 있습니다

---

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        queue<pair<int, pair<int, vector<int>>>> q; // {acc, {idx, combination}}

        for (int i = 0; i < candidates.size(); i++) {
            int num = candidates[i];

            if (num <= target) {
                vector<int> comb;
                comb.push_back(num);
                q.push({num, {i, comb}});
            }

        }

        while (!q.empty()) {
            auto p = q.front();
            q.pop();

            int acc = p.first, idx = p.second.first;
            auto comb = p.second.second;

            if (acc == target) {
                res.push_back(comb);
            } else if (acc < target) {
                for (int i = idx; i < candidates.size(); i++) {
                    int num = candidates[i];

                    if (acc + num <= target) {
                        vector<int> new_comb(comb);
                        new_comb.push_back(num);
                        q.push({acc + num, {i, new_comb}});
                    }
                }
            }
        }

        return res;
    }
};
```
