import java.util.List;
import java.util.ArrayList;
/**
 중복 되지 않은 요소들이 들어있는 candidates 배열이 주어지고 target 값이 주어진다.
 합이 target과 같은 중복되지 않은 조합을 모두 반환하시오.
 */
class Solution {

    List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        combination(0, candidates, target, 0, new ArrayList<>());
        return answer;
    }

    // 시간복잡도 O(2^target)
    public void combination(int idx, int[] candidates, int target, int currentSum, List<Integer> comb) {
        // 누적 합이 넘으면
        if (currentSum > target) {
            return;
        }

        // 누적 합이 타겟 값과 같으면
        if (currentSum == target) {
            answer.add(new ArrayList<>(comb));
            return;
        }

        for (int i = idx; i < candidates.length; i++) {
            comb.add(candidates[i]);
            combination(i, candidates, target, currentSum + candidates[i], comb);
            comb.remove(comb.size() - 1);
        }
    }
}

