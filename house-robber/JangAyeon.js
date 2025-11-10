/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const N = nums.length;
  let answer = 0;
  function dfs(lastVisited, curr, t) {
    if (curr == N) {
      console.log(t);
      answer = Math.max(answer, t);
      return;
    }
    for (let idx = curr; idx < N; idx++) {
      if (idx != lastVisited + 1) {
        dfs(idx, idx + 1, t + nums[idx]);
      }
      dfs(lastVisited, idx + 1, t);
    }
  }
  dfs(-2, 0, 0);
  return answer;
};
