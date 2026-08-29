// 문제풀이 흐름
// 하나를 집어넣고, 모자라면 이전과 동일한걸 집어넣거나 더 큰걸 집어넣는 방식으로 계속 확인
// -> 백트래킹 방식

// n = candidates.length / m = candidates[0] 라 할때,
// 시간복잡도 :
//      이론상 O(n ^ (target / m))
//      150 조합 이내로 뽑히게끔 만들어뒀으므로 알아서 잘되지 않았을까...
// 공간복잡도 :
//      O(target / m) - 재귀 깊이만큼


class Solution {

	List<List<Integer>> answer = new ArrayList<>();
	int[] candidates;
	int target;

	public List<List<Integer>> combinationSum(int[] candidates, int target) {
		this.candidates = candidates;
		this.target = target;

		backtracking(new ArrayList<>(), 0, target);
		return answer;
	}

	public void backtracking(List<Integer> combination, int currentIdx, int remainder) {
		if (remainder == 0) {
			answer.add(new ArrayList<>(combination));
			return;
		} else if (remainder < 0) {
			return;
		}

		for (int i = currentIdx ; i < candidates.length ; i++) {
			combination.add(candidates[i]);
			backtracking(combination, i, remainder - candidates[i]);
			combination.remove(combination.size() - 1);
		}
	}
}
