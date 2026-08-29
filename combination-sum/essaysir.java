import java.util.*;

class Solution {
	public List<List<Integer>> combinationSum(int[] candidates, int target) {
		// 합이 target 이 되는 경우의 수를 모두 고르시오
		// target 이 150 이하
		List<List<Integer>> result = new ArrayList<>();
		List<Integer> current = new ArrayList<>();

		backTracking(candidates, target, 0 , result, current);
		return result;
	}

	public void backTracking(int[] candidates, int remain, int start, List<List<Integer>> result, List<Integer> current) {
		if ( remain == 0 ){
			result.add(new ArrayList<>(current));
			return;
		}

		if ( remain < 0 ){
			return;
		}

		for (int i = start; i < candidates.length; i++) {
			current.add(candidates[i]);

			backTracking(candidates, remain - candidates[i], i , result, current); 

			current.remove(current.size() - 1);
		}
	}
}
