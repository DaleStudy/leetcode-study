/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

// C = candidates, T = target, m = smallest candidate value
// TC: O(C^(T/m)) -> 후보와 타겟 깊이 간 지수적 증가
// SC: O(T/m) -> 재귀 스택 깊이 (*출력 결과는 복잡도 계산 제외)
var combinationSum = function (candidates, target) {
  const result = [];

  function go(candi, combi, acc, start) {
    if (acc === target) {
      result.push(combi);
      return;
    }

    for (let i = start; i < candi.length; i++) {
      const newAcc = acc + candi[i];
      const newCombi = [...combi, candi[i]];
      if (newAcc > target) break;
      go(candi, newCombi, newAcc, i);
    }
  }

  go(
    [...candidates].sort((a, b) => a - b), // 값 순서 보장으로 새로운 누적 값에서 조기 종료 가능. 오름차순에 따라 newAcc가 target을 넘어가면 이후의 후보들은 계산할 필요 없음.
    [],
    0,
    0,
  );

  return result;
};
