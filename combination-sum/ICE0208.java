import java.util.ArrayList;
import java.util.List;

class Solution {
    /*
    * [백트래킹 풀이]
    * N: candidates의 길이
    * M: candidates에서 가장 작은 값
    *
    * 시간 복잡도: O(N^(target / M))
    * - 재귀 한 단계에서 최대 N개의 후보를 선택할 수 있다.
    * - 가장 작은 숫자를 반복해서 선택하면 재귀 깊이는 최대 target / M이다.
    * - 실제로는 startIndex와 가지치기로 인해 이보다 적은 경우만 탐색한다.
    *
    * 공간 복잡도: O(target / M)
    * - 재귀 호출 스택과 현재 조합 리스트가 최대 재귀 깊이만큼 사용된다.
    * - 반환할 결과 리스트는 제외한다.
    */

    private int[] candidates;
    private List<List<Integer>> combinations;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.candidates = candidates;
        this.combinations = new ArrayList<>();

        findCombinations(0, target, new ArrayList<>());

        return combinations;
    }

    private void findCombinations(
            int startIndex,
            int remainingTarget,
            List<Integer> currentCombination
    ) {
        // 목표 합을 정확히 완성한 경우
        if (remainingTarget == 0) {
            combinations.add(new ArrayList<>(currentCombination));
            return;
        }

        for (int i = startIndex; i < candidates.length; i++) {
            int candidate = candidates[i];

            // 현재 숫자를 선택하면 목표 합을 초과하는 경우
            if (candidate > remainingTarget) {
                continue;
            }

            currentCombination.add(candidate);

            // 같은 숫자를 여러 번 사용할 수 있으므로 i부터 다시 탐색한다.
            findCombinations(
                    i,
                    remainingTarget - candidate,
                    currentCombination
            );

            // 다음 조합을 탐색하기 위해 현재 선택을 되돌린다.
            currentCombination.remove(currentCombination.size() - 1);
        }
    }
}
