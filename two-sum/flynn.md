## Description

`key: num, value: index`를 저장할 hashmap을 선언합니다.

배열 `nums`의 첫번째 원소를 hashmap에 저장합니다. (`nums[0]: 0`)

배열 `nums`를 두번째 원소부터 조회하여 `target - nums[i]`가 hashmap에 존재하는지 판단합니다.

만약 `target - nums[i]`가 hashmap에 존재한다면 정답 배열을 반환하고, 그렇지 않다면 hashmap에 새로운 쌍을 추가합니다.

## Big-O

주어진 배열 `nums`의 크기 N에 대해,

Time complexity: `O(N)`

- 배열 `nums`를 순회하기 때문에 `O(N)`의 시간 복잡도를 가집니다.

Space complexity: `O(N)`

- hashmap의 크기가 배열 `nums`의 크기에 가깝게 커질 수 있으므로 `O(N)`의 공간복잡도를 가집니다.

---

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> past; // key: num value: index
        vector<int> res;

        past.insert({nums[0], 0});

        for (int i = 1; i < nums.size(); i++) {
            int remainder = target - nums[i];

            if (past.find(remainder) != past.end()) {
                res.push_back(i);
                res.push_back(past[remainder]);
                break;
            } else {
                past.insert({nums[i], i});
            }
        }

        return res;
    }
};
```
