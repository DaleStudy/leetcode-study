import java.util.ArrayList;
import java.util.List;

// backtracking
// 시간복잡도: 각 배열 원소마다 target을 만드는 데에 기여를 할 수도 있고 안 할 수도 있음 -> O(2^(target))
// 공간복잡도: O(k * t) (k는 가능한 조합의 수, t는 각 조합의 크기)

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int target, int start, List<Integer> currentCombination, List<List<Integer>> result) {
        // 목표값에 도달하면 현재 조합을 결과에 추가
        if (target == 0) {
            result.add(new ArrayList<>(currentCombination));
            return;
        }

        // 후보 숫자들을 탐색
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > target) continue; // 목표값보다 큰 숫자는 넘어감

            currentCombination.add(candidates[i]); // 현재 숫자를 선택
            // 현재 숫자를 다시 사용할 수 있기 때문에 i를 그대로 두고 재귀 호출
            backtrack(candidates, target - candidates[i], i, currentCombination, result);
            currentCombination.remove(currentCombination.size() - 1); // 백트래킹: 마지막 숫자 제거
        }
    }
}

class newSolution{
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> tempList, int[] candidates, int remain, int start) {
        if (remain < 0) return;         // 넘치면 종료
        if (remain == 0) {
            result.add(new ArrayList<>(tempList)); // 정답 조합 발견
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            tempList.add(candidates[i]); // 후보 추가
            backtrack(result, tempList, candidates, remain - candidates[i], i); // **같은 수를 다시 사용할 수 있으므로 i**
            tempList.removeLast(); // 백트래킹 (되돌리기)
        }
    }
}
