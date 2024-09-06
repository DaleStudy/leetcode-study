/**
 * 풀이
 * - 주어진 배열 `nums`를 순서대로 조회합니다
 * - 0과 음수를 곱하는 경우를 고려하기 위해 현재 subarray의 곱의 최대값뿐만 아니라 최소값 또한 기록합니다
 * 
 * Big-O
 * - N: 주어진 배열 `nums`의 size
 * 
 * - Time complexity: O(N)
 * - Space complexity: O(1)
 */

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_prod = nums[0];
        int min_prod = nums[0];
        int res = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            int curr = nums[i];

            int tmp_max = max(curr, max(curr * max_prod, curr * min_prod));
            min_prod = min(curr, min(curr * max_prod, curr * min_prod));
            max_prod = tmp_max;

            res = max(res, max_prod);
        }

        return res;
    }
};
