/**
 * 문제 유형
 * - DP: DFS + Backtracking
 *
 * 문제 설명
 * - 주어진 숫자 배열에서 조합을 만들어서 합이 target이 되는 경우를 찾기
 *
 * 아이디어
 * 1) Backtracking 활용
 * - dfs를 통해 합이 target이 되는 모든 케이스를 탐색한다. (단, 조건 체크 후에 즉시 중단 = 백트래킹)
 */
function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  function backtracking(
    startIndex: number,
    combination: number[],
    total: number
  ) {
    if (total === target) {
      result.push([...combination]);
      return;
    }

    if (total > target) return;

    for (let i = startIndex; i < candidates.length; i++) {
      combination.push(candidates[i]);
      backtracking(i, combination, total + candidates[i]);
      combination.pop();
    }
  }

  backtracking(0, [], 0);
  return result;
}
