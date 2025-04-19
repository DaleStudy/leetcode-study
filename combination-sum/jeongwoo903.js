/*
* k: 후보 수
* t: target / 최소 숫자
* 시간 복잡도: O(k^t)
* 공간 복잡도; O(k^t * t)
*/

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

var combinationSum = function(candidates, target) {
  const combine = (sum, path, startIndex) => {
    if (sum > target) return [];
    if (sum === target) return [path];

    return candidates
    .slice(startIndex)
    .flatMap((candidate, i) =>
      combine(sum + candidate, [...path, candidate], startIndex + i)
    );
  };

  return candidates.flatMap((candidate, i) =>
    combine(candidate, [candidate], i)
  );
};
