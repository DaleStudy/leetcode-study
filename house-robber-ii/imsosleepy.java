// house robber 1이 dp문제여서 dp문제라는거 알 수 있었음
// 시작점을 다르게 해서 두개의 dp를 결합하는 아이디어는 맞았음(첫 집을 털었을때, 마지막 집을 털었을 때)
// 구현이 너무 오래걸려서 GPT의 도움을 받음.. 
// DP는 아이디어가 절반이라 생각했는데 구현을 잘 못해서 아쉬움
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0]; // 집이 하나면 그 집만 털면 됨.

        int n = nums.length;
        
        // 1. 첫 번째 집을 포함하지 않는 경우 (nums[1] ~ nums[n-1])
        int[] dp1 = new int[n]; 
        dp1[0] = 0; // 첫 번째 집을 포함하지 않으므로 0
        dp1[1] = nums[1]; // 두 번째 집을 털었을 경우

        for (int i = 2; i < n; i++) {
            dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i]);
        }

        // 2. 마지막 집을 포함하지 않는 경우 (nums[0] ~ nums[n-2])
        int[] dp2 = new int[n];
        dp2[0] = nums[0]; // 첫 번째 집을 털었을 경우
        dp2[1] = Math.max(nums[0], nums[1]); // 두 번째 집을 털지 않을 수도 있음

        for (int i = 2; i < n - 1; i++) {
            dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + nums[i]);
        }

        return Math.max(dp1[n - 1], dp2[n - 2]);
    }
}
