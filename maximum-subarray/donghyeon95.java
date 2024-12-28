import java.util.Arrays;

class Solution {
	public int maxSubArray(int[] nums) {
		int max = Integer.MIN_VALUE;
		int current = 0;

		for (int num: nums) {
			System.out.println(num + " " +max);
			if (current + num >=0) {
				max = Math.max(max, current+num);
				current = current+num;
			} else {
				current = 0;
			}
		}

		// 전부 음수일 경우 => 가장 큰수 return
		return max>=0? max:  Arrays.stream(nums).max().getAsInt();
	}
}

