// 시간복잡도: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const n = nums.length;
  if (n === 0) return 0;
  if (n === 1) return nums[0];

  // DP 배열 초기화
  let prev2 = 0; // dp[i-2]
  let prev1 = 0; // dp[i-1]

  // 최대 수익 계산
  for (let num of nums) {
    const current = Math.max(prev1, prev2 + num);
    prev2 = prev1;
    prev1 = current;
  }

  return prev1;
};
