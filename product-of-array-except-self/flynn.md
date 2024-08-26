## Description

한 칸씩 밀린 상태로 누적곱을 배열에 기록해주는 것을 두 번 진행해주면 원하는 바를 얻을 수 있습니다.

| index | 0         | 1         | 2         | 3         |
| ----- | --------- | --------- | --------- | --------- |
| value | 1         | 2         | 3         | 4         |
| acc-> |           | 1         | 1 x 2     | 1 x 2 x 3 |
| <-acc | 2 x 3 x 4 | 3 x 4     | 4         |           |
| res   | 2 x 3 x 4 | 1 x 3 x 4 | 1 x 2 x 4 | 1 x 2 x 3 |

## Big-O

Time complexity: O(N)

Space complexity: O(N)

---

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 1);

        for (int i = 1; i < nums.size(); i++) {
            res[i] *= nums[i - 1] * res[i - 1];
        }

        int acc = 1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            acc *= nums[i + 1];
            res[i] *= acc;
        }

        return res;
    }
};
```
