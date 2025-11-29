/**
 * Combination Sum
 *
 * 핵심 아이디어:
 * - DFS + 백트래킹으로 모든 조합 탐색
 * - 같은 숫자를 여러 번 사용 가능
 * - start 인덱스로 중복 조합 방지 ([2,3]과 [3,2] 같은 것)
 *
 * 시간 복잡도: O(N^(T/M)) - N: 후보 개수, T: 타겟, M: 최소값
 * 공간 복잡도: O(T/M) - 재귀 깊이
 */

const combinationSum = (candidates, target) => {
  const result = [];

  const dfs = (remain, start, path) => {
    // Base case: 타겟 달성
    if (remain === 0) {
      result.push([...path]); // 현재 경로 저장
      return;
    }

    // Base case: 타겟 초과 (pruning)
    if (remain < 0) return;

    // 모든 후보 탐색
    for (let i = start; i < candidates.length; i++) {
      // 가지치기: 남은 값보다 크면 스킵
      if (candidates[i] > remain) continue;

      // 선택
      path.push(candidates[i]);

      // 탐색 (i부터 시작 - 같은 숫자 재사용 가능)
      dfs(remain - candidates[i], i, path);

      // 되돌리기 (백트래킹)
      path.pop();
    }
  };

  dfs(target, 0, []);
  return result;
};
