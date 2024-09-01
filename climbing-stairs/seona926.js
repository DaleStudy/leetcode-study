/**
 * @param {number} n
 * @return {number}
 */
let climbStairs = function (n) {
  if (n <= 1) return 1;

  let ways = new Array(n + 1);
  ways[0] = 1;
  ways[1] = 1;

  for (let i = 2; i <= n; i++) {
    ways[i] = ways[i - 1] + ways[i - 2]; // 점화식 사용
  }

  return ways[n];
};

/*
  1. 시간 복잡도: O(n)
    - for 루프의 시간 복잡도
  2. 공간 복잡도: O(n)
    - 배열 ways의 공간 복잡도
*/
