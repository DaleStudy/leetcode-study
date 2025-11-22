/**
 * @param {number} n
 * @return {number}
 * 
 * 시간복잡도 계산
 * 메모이제이션으로 n번째에는 n번째에 대한 부분만 연산되므로 O(n)
 * 
 * 공간복잡도 계산
 * memo배열에 n번째 연산값들이 각 인덱스에 할당되므로 O(n)
d */

var climbStairs = function (n, memo = []) {
  if (memo[n] !== undefined) return memo[n];

  if (n <= 1) return 1;

  memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo);

  return memo[n];
};
