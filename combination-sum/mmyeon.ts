/**
 * 접근 방법 :
 *  - 중복 포함하여 모든 조합 구해야 하니까 재귀함수로 풀기
 *  - 재귀 호출로 탐색해야하는 타겟 줄여가면서 조합 만들기
 *  - 동일 조합추가되지 않도록, startIndex 추가하여 다음 인덱스부터 순회하도록 제한
 *
 *
 * 시간복잡도 : O(n^target)
 * -  candidates 배열 길이 n만큼 재귀가 호출되고, 각 호출은 target 길이 만큼 중첩되니까 O(n^target)
 *
 * 공간복잡도 : O(target)
 *  - 최악의 경우 target만큼 재귀 호출되니까 O(target)
 *
 */

function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  const dfs = (target: number, combination: number[], startIndex: number) => {
    if (target === 0) {
      result.push([...combination]);
      return;
    }

    if (target < 0) return;

    for (let i = startIndex; i < candidates.length; i++) {
      combination.push(candidates[i]);
      dfs(target - candidates[i], combination, i);
      combination.pop();
    }
  };

  dfs(target, [], 0);

  return result;
}
