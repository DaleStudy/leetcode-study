/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  const answer = [];
  const n = candidates.length;
  const combi = (i, sum, arr) => {
    for (let j = i; j < n; j++) {
      const candidate = candidates[j];
      const newSum = sum + candidate;

      if (newSum === target) {
        answer.push([...arr, candidate]);
        continue;
      }

      if (newSum > target) {
        continue;
      }

      if (newSum < target) {
        combi(j, newSum, [...arr, candidate]);
      }
    }
  };

  combi(0, 0, []);

  return answer;
};
