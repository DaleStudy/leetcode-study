import java.util.Arrays;

class Solution {
	private int[] dp;

	public int rob(int[] nums) {
		// 점화식
		// f(x) = f(나를 선택) + f(나를 안선택)
		// 100개라서 가능은 할 거 같다.

		dp = new int[100];

		// 0도 가능 하다
		Arrays.fill(dp, -1);


		return recurse(nums, 0);

	}

	public int recurse(int[] nums, int index) {
		// 종료 조건
		if (index >= nums.length) return 0;

		// 이미 한번 처리가 되었다면
		if (dp[index] != -1) return dp[index];

		int result = 0;

		// 나를 선택하는 경우,
		result = Math.max(recurse(nums, index+2)+nums[index], result);

		// 나를 선택하지 않는 경우,
		result = Math.max(recurse(nums, index+1), result);

		dp[index] = result;
		return result;
	}
}

