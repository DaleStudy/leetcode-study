/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
function combinationSum(candidates, target) {
  var buffer = [];
  var result = [];
  search(0, target);
  return result;

  function search(startIdx, target) {
    if (target === 0) return result.push(buffer.slice());
    if (target < 0) return;
    if (startIdx === candidates.length) return;
    buffer.push(candidates[startIdx]);
    search(startIdx, target - candidates[startIdx]);
    buffer.pop();
    search(startIdx + 1, target);
  }
};

