import java.util.*;

class Solution {
	public int[] twoSum(int[] nums, int target) {
		// TWO Sum , 순서는 상관이 없음. NC2 를 계산 필요
		int[] result = new int[2];
		for ( int i = 0; i < nums.length; i++){
			for ( int j = i + 1; j < nums.length; j++){
				if ( target == nums[i] + nums[j]){
					result[0] = i;
					result[1] = j;
				}
			}
		}
		return result;
	}
}