/**
 * [풀이 개요]
 * - 시간복잡도 : O(H(N, M) * M)
 * - 공간복잡도 : O(H(N, M) * M) (정답 배열 제외 시 O(M))
 */
class Solution {
    /**
     * [문제 풀이 아이디어]
     * - candidates 배열의 수를 조합해서 target을 만드는 조합을 중복되는 조합 없이 찾아야 함.
     * - 각 원소는 중복이 될 수 있음. 이 때문에 candidates을 여러번 반복해서 찾아야 함. 조합이 되는 배열의 길이가 동적이므로 재귀적으로 확인해야 할 듯.
     * - 시공간복잡도의 경우, 중복 조합의 개수를 계산해야 하는 건 알겠는데, 계산이 직관적으로는 이해가 잘 안됨. O(H(N, M) * M)
     */
    private List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        backtracking(0, 0, target, candidates, new ArrayList<>());
        return answer;
    }

    /**
     * [시뮬레이션: 인덱스 & Sum 추적]
     * 형식: [인덱스 조합] (계산 과정) = 현재Sum
     * * * 시작 (Sum = 0)
     * ├── [0] (+2) = Sum: 2
     * │    ├── [0, 0] (+2) = Sum: 4
     * │    │    ├── [0, 0, 0] (+2) = Sum: 6
     * │    │    │    └── [0, 0, 0, 0] (+2) = Sum: 8 ❌ (Over 7)
     * │    │    └── [0, 0, 1] (+3) = Sum: 7 ★ 정답 [2, 2, 3]
     * │    ├── [0, 1] (+3) = Sum: 5
     * │    │    └── [0, 1, 1] (+3) = Sum: 8 ❌ (앞의 2로 못 돌아감)
     * │    └── [0, 2] (+6) = Sum: 8 ❌
     * │
     * ├── [1] (+3) = Sum: 3  <-- 이제 이전 인덱스인 0번(값 2)은 영구 제외
     * │    ├── [1, 1] (+3) = Sum: 6
     * │    │    └── [1, 1, 1] (+3) = Sum: 9 ❌
     * │    └── [1, 2] (+6) = Sum: 9 ❌
     * │
     * ├── [2] (+6) = Sum: 6
     * │    └── [2, 2] (+6) = Sum: 12 ❌
     * │
     * └── [3] (+7) = Sum: 7 ★ 정답 [7]
     */
    public void backtracking(int start, int sum, int target, int[] candidates, List<Integer> list) {
        if(sum == target) {
            answer.add(new ArrayList<>(list));
            return; // 🎯 정답을 찾았으므로 즉시 탈출 (효율성 증가)
        }
        
        if(sum > target) {
            return;
        }

        // 🎯 i = start 및 재귀 인자 i로 변경하여 주석의 '중복 조합' 로직 완성
        for(int i = start; i < candidates.length; i++) {
            list.add(candidates[i]);
            backtracking(i, sum + candidates[i], target, candidates, list);
            list.remove(list.size() - 1);
        }
    }
}
