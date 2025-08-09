/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  const result = [];
  candidates.sort((a, b) => a - b);
  function backTracking(start, arr, total) {
    if (total == target) {
      result.push([...arr]);
      return;
    }

    for (let i = start; i < candidates.length; i++) {
      const cur = candidates[i];
      if (cur + total > target) {
        return;
      }

      backTracking(i, [...arr, cur], total + cur);
    }
  }

  backTracking(0, [], 0);
  return result;
};
