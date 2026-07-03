class Solution {
	public int rob(int[] nums) {
		int prev = 0;  // dp[i-2]: 두 칸 전까지의 최대 금액
		int curr = 0;  // dp[i-1]: 한 칸 전까지의 최대 금액

		for (int num : nums) {
			// 현재 집을 털 경우(prev + num) vs 안 털 경우(curr) 중 큰 값
			int temp = Math.max(curr, prev + num);
			prev = curr;
			curr = temp;
		}

		return curr;
	}
}
