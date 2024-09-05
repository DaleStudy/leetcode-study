/**
 *  알고리즘: 백트랙킹
 *  시간 복잡도: O(n^t)
 *  - n: candidates.lenth
 *  - t: target / candidates의 최솟값
 *  - 예시를 통해 시간 복잡도를 이해해보자!
 *
 *  - candidates: [2, 3], target: 6
 *    - [2] -> [2, 2] -> [2, 2, 2] -> OK (여기서 생각해보면, 아 재귀를 최대 6/2 만큼 타고 들어가겠군?)
 *    - [2, 2] -> [2, 2, 3] -> X
 *    - [2] -> [2, 3] -> [2, 3, 3] -> X
 *    - [3] -> [3, 3] -> OK
 *  - 중간에 sum > target, sum == target 인 경우 return 하기 때문에 모든 케이스를 다 검사하진 않지만
 *  - 기본적으로 아래와 같이 문제를 풀게 될 경우 최악의 경우에는 O(n^t) 만큼 소요된다.
 *
 *  공간 복잡도: O(t)
 *  - t: target / candidates의 최솟값
 *  - 이것도 생각해보니까 주어진 candidates.length (=n) 값에 비례하는 게 아니라
 *  - (가능한 케이스에서) 가장 작은 값으로 타겟을 채우는 게 가장 많은 사이즈를 차지하는 값이 될텐데, 이것에 영향을 받겠군.
 *
 */
class Solution {

    private List<List<Integer>> answer = new ArrayList<>();
    private List<Integer> combination = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        backtracking(candidates, target, 0, 0);
        return answer;
    }

    private void backtracking(int[] candidates, int target, int sum, int start) {
        if (sum > target) {
            return;
        }
        if (sum == target) {
            answer.add(new ArrayList<>(combination));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            combination.add(candidates[i]);
            backtracking(candidates, target, sum + candidates[i], i);
            combination.remove(combination.size() - 1);
        }
    }
}
