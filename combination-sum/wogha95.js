// 2차
// 몫을 활용하여 시간복잡도를 줄이고자 하였으나 generateSubResult에서 추가 시간발생으로 유의미한 결과를 발견하지 못했습니다.
// TC: O(C^2 * T)
// SC: O(T)
// C: candidates.length, T: target

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  const result = [];
  // 'q' means 'quotient'.
  const qList = candidates.map((candidate) => Math.floor(target / candidate));

  dfs([], 0);

  return result;

  function dfs(selectedQList, total) {
    if (total > target) {
      return;
    }

    if (total === target) {
      result.push(generateSubResult(selectedQList));
      return;
    }

    const currentIndex = selectedQList.length;
    for (let q = qList[currentIndex]; q >= 0; q--) {
      selectedQList.push(q);
      dfs(selectedQList, total + candidates[currentIndex] * q);
      selectedQList.pop();
    }
  }

  function generateSubResult(selectedQList) {
    return selectedQList
      .map((q, index) => new Array(q).fill(candidates[index]))
      .flat();
  }
};

// 1차
// dfs를 활용하여 각 요소를 추가 -> 재귀 -> 제거로 순회합니다.
// TC: O(2^C)
// SC: O(T)
// C: candidates.length, T: target

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  const result = [];

  dfs([], 0, 0);

  return result;

  function dfs(subResult, total, currentIndex) {
    if (total > target) {
      return;
    }

    if (total === target) {
      result.push([...subResult]);
      return;
    }

    if (currentIndex === candidates.length) {
      return;
    }

    const candidate = candidates[currentIndex];
    subResult.push(candidate);
    dfs(subResult, total + candidate, currentIndex);
    subResult.pop();
    dfs(subResult, total, currentIndex + 1);
  }
};
