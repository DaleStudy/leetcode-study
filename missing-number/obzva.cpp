/**
 * 풀이
 * - 특정 정수가 `nums` 배열을 통해 주어졌는지 여부를 체크하는 배열 `check`를 만듭니다
 * - `nums`를 조회하며 `check`배열의 값들을 변경합니다
 * - `check`배열을 조회하여 누락되었던 정수를 확인합니다
 * 
 * Big-O
 * - N: 주어진 배열 `nums`의 크기
 * 
 * - Time Complexity: O(N)
 *   - 배열 `nums`를 조회하는 반복문은 O(N)의 시간 복잡도를 가집니다
 *   - 배열 `check`를 조회하는 반복문 또한 O(N)의 시간 복잡도를 가집니다
 *   - 따라서 전체 시간 복잡도는 O(N)입니다
 * 
 * - Space Complexity: O(N)
 *   - `check`배열의 크기가 입력값에 비례하여 선형적으로 증가합니다
 */

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        
        vector<bool> check(n + 1, false);

        for (auto num : nums) check[num] = true;

        int res;
        for (int i = 0; i < n + 1; i++) {
            if (!check[i]) {
                res = i;
                break;
            }
        }

        return res;
    }
};
