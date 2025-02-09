/*
time complexity: O(n)
space complexity: O(1)

왼쪽에서부터 누적합을 구하되, 더한 값이 음수가 되는 순간 지금까지 더한 값을 버린다. (즉, 지금까지의 원소는 모두 subarray에서 제외한다.) 이렇게 누적합을 계산하면서, 누적합의 최대값을 찾으면 답이 된다.

단, 모든 원소가 음수인 경우는 예외적으로 처리해준다.

*/

class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int ans = -10001;
        int max = -10001;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (sum + nums[i] < 0) {
                sum = 0;
            } else {
                sum += nums[i];
            }
            if (sum > ans) {
                ans = sum;
            }
            if (max < nums[i]) {
                max = nums[i];
            }
        }

        // 모두 음수인 경우의 예외 처리
        if (max < 0) {
            return max;
        } else {
            return ans;
        }
    }
}
