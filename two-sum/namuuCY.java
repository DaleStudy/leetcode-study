// 문제 풀이 흐름
// target이 고정되어있고, 이 target에서 현재 값을 뺀게 존재하는지를 확인해야함.
// 존재한다면, 그 값의 인덱스를 바로 알아야 함.
// hashmap을 사용

// N = nums.length 라 하면
// 시간복잡도 : O(N)
// 공간복잡도 : O(N)

class Solution {
	public int[] twoSum(int[] nums, int target) {
		Map<Integer, Integer> numberCount = new HashMap<>();

		for (int i = 0 ; i < nums.length; i ++) {
			int val = target - nums[i];
			if (numberCount.containsKey(val)) {
				return new int[]{i, numberCount.get(val)};
			}

			numberCount.put(nums[i], i);
		}

		return null;
	}
}
