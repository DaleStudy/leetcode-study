import java.util.HashSet;

class Solution {
	public boolean containsDuplicate(int[] nums) {
		HashSet<Integer> arr = new HashSet<Integer>();
		boolean answer = false;

		for(int num : nums){
			arr.add(num);
		}

		if(nums.length != arr.size()){
			answer = true;
		}

		return answer;
	}
}
