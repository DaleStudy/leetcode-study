import java.util.HashMap;
import java.util.HashSet;

class Solution {
	public int[] twoSum(int[] nums, int target) {
		// // O(N^2)
		// for (int i =0; i< nums.length-1; i++) {
		// 	for (int j=i+1;  j<nums.length; j++) {
		// 		if (nums[i] + nums[j] == target)
		// 			return new int[] {i, j};
		// 	}
		// }
		// return null;

		// O(N)
		// HashMap 사용
		HashMap<Integer, Integer> map = new HashMap<>();
		for (int i=0; i<nums.length; i++) {
			map.putIfAbsent(nums[i], i);
		}

		for (int i=0; i<nums.length; i++) {
			int num = nums[i];
			int anoterNum = target - num;
			if (map.containsKey(anoterNum) && i!=map.get(anoterNum))
				return new int[] {i, map.get(anoterNum)};
		}
		return null;
	}
}

