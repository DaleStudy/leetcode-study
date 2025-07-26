import java.util.HashMap;

public class leebeanbin {
	public static int[] bruteForce(int[] nums, int target) {
		for (int i = 0; i < nums.length; i++) {
			for (int j = i + 1; j < nums.length; j++) {
				if (nums[i] + nums[j] == target) {
					return new int[]{i, j};
				}
			}
		}
		return null;
	}

	public static int[] hashMap(int[] nums, int target) {
		HashMap<Integer, Integer> arr = new HashMap<>();

		for (int i = 0; i < nums.length; i++) {
			arr.put(nums[i], i);

			if (arr.containsKey(target - nums[i])) {
				return new int[]{arr.get(target - nums[i]), i};
			}
		}

		return null;
	}
}
