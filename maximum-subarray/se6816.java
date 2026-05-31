/**
	dp를 이용하여 지속적으로 최대의 값을 기록하면서 연속 부분 배열의 최대 합을 구하는 방식
	nums 의 길이 -> N
	시간 복잡도 : O(N)
	공간 복잡도 : O(N)
 */
class Solution2 {
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        for(int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(nums[i], dp[i-1] + nums[i]);
        }

        for(int i = 0; i < dp.length; i++) {
        }
        return Arrays.stream(dp)
                .max()
                .getAsInt();
    }
}

/**
	이전 방식과 동일하나 변수 하나로 이전 값만 유지하는 방식
	nums 의 길이 -> N
	시간 복잡도 : O(N)
	공간 복잡도 : O(1)
 */
class Solution {
    public int maxSubArray(int[] nums) {
        int prevSum = nums[0];
        int result = prevSum;
        for(int i = 1; i < nums.length; i++) {
            prevSum = Math.max(nums[i], prevSum + nums[i]);
            result = Math.max(result, prevSum);
        }

        return result;
    }
}
