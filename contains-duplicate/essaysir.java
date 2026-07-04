import java.util.*;

class Solution {
	public boolean containsDuplicate(int[] nums) {
		Set<Integer> sets = new HashSet<>();
		for ( int i = 0; i < nums.length; i++){
			boolean added = sets.add(nums[i]);
			if (!added) return true;
		}
		return false;
	}
}
