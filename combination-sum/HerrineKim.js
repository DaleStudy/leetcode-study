// 시간 복잡도 : O(n^2)
// 공간 복잡도 : O(n)

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

var combinationSum = function(candidates, target) {
  const result = [];
  
  const backtrack = (remaining, combo, start) => {
      if (remaining === 0) {
          result.push([...combo]);
          return;
      }
      
      for (let i = start; i < candidates.length; i++) {
          if (candidates[i] <= remaining) {
              combo.push(candidates[i]);
              backtrack(remaining - candidates[i], combo, i);
              combo.pop();
          }
      }
  };
  
  backtrack(target, [], 0);
  return result;
};