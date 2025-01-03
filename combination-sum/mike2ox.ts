/**
 * source: https://leetcode.com/problems/combination-sum/
 * 풀이방법: 재귀를 이용하여 모든 조합을 탐색
 *
 * 시간복잡도: O(n^m) (n: candidates의 길이, m: target을 만들기 위한 최대 반복 횟수)
 * 공간복잡도: O(n^m) (n: candidates의 길이, m: target을 만들기 위한 최대 반복 횟수)
 *
 * Note
 * - 당장에 구현하려다보니 재귀를 이용한 방법으로 구현. => 추후 리팩토링 필요
 */
function combinationSum(candidates: number[], target: number): number[][] {
  if (target === 0) return [[]];
  if (target < 0) return [];

  const result: number[][] = [];

  for (let i = 0; i < candidates.length; i++) {
    const num = candidates[i];
    const subCombos = combinationSum(candidates.slice(i), target - num);

    for (const combo of subCombos) {
      result.push([num, ...combo]);
    }
  }

  return result;
}
