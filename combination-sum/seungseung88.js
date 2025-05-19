/**
 * 시간복잡도: O(2^n)
 * 공간복잡도: O(target)
 */

function combinationSum(canditates, target) {
  const result = [];
  const nums = [];

  function dfs(start, total) {
    if (total > target) return;
    if (total === target) result.push([...nums]);

    // 중복제거를 위해 start로 시작
    for (let i = start; i < canditates.length; i += 1) {
      num = canditates[i];
      nums.push(num);
      dfs(i, total + num);
      nums.pop();
    }
  }

  // 시작 인덱스, 누적 합
  dfs(0, 0);

  return result;
}
