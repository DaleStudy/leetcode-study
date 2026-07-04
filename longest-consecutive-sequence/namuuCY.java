// 문제 풀이 흐름
// 오름차순 sort 후에 현재 보고 있는 숫자가 이전 숫자와
// 같으면 count 유지
// 1차이나면 count 증가
// 이외에는 count 초기화 및 이전 count 최댓값 비교

// N = nums.length 라 할때
// 시간복잡도 : O(N logN)
// 공간복잡도 : O(N)

class Solution {
	public int longestConsecutive(int[] nums) {
		Arrays.sort(nums);

		if (nums.length == 0) return 0;

		int maxSequenceLength = 0;
		int currentLength = 1;

		for (int i = 1 ; i < nums.length; i ++) {
			if (nums[i] == nums[i - 1]) continue;
			if (nums[i] == nums[i - 1] + 1) {
				currentLength ++;
				continue;
			}

			maxSequenceLength = Math.max(maxSequenceLength, currentLength);
			currentLength = 1;
		}

		return Math.max(maxSequenceLength, currentLength);
	}
}
