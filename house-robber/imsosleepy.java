// 점화식의 최대값을 구하는 방법
// 1. 현재 위치의 최대 값은 한칸 전 집까지만 털었던가(두칸 연속 겹치면 안된다는 룰을 지키면서)
// 2. 두칸 전 집까지 털고 + 현재집을 털었을 때다
// 공간복잡도를 줄이는법. 배열로 관리 안하기
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];

        int prev2 = nums[0]; // dp[i-2]
        int prev1 = Math.max(nums[0], nums[1]); // dp[i-1]
        for (int i = 2; i < nums.length; i++) {
            int current = Math.max(nums[i] + prev2, prev1);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
