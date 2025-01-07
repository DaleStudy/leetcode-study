import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

// O(N)
class Solution {
	public int missingNumber(int[] nums) {
		Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());

		for (int i=0; i<nums.length; i++) {
			if (!numSet.contains(i)) return i;
		}

		return nums.length;
	}
}

