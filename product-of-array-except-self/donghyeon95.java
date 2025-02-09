class Solution {
	public int[] productExceptSelf(int[] nums) {
		int[] result = new int[nums.length];
		int[] right = new int[nums.length];
		int[] left = new int[nums.length];

		// -> 이쪽 방향으로 한번 계산
		right[0] = nums[0];
		for (int i=1; i<nums.length; i++) {
			right[i] = right[i-1]*nums[i];
		}

		// <- 이쪽 방향으로 한번 계산
		left[nums.length-1] = nums[nums.length-1];
		for (int i=nums.length-2; i>-1; i--) {
			left[i] = left[i+1]*nums[i];
		}

		// f(i) = right(i-1) * left(i+1)
		result[0] = left[1];
		result[nums.length-1] = right[nums.length-2];
		for (int i=1; i<nums.length-1; i++) {
			result[i] = right[i-1] * left[i+1];
		}

		return result;
	}

	// 2 포인터를 활용하면 O(1)가능
}

