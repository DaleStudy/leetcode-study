/**
 * 시간복잡도: O(n)
 *  - for문 O(n)
 * 공간복잡도: O(n)
 *  - arr O(n)
 */
const climbStairs = (n) => {
  const arr = [1, 2];

  for (let i = 2; i < n; i += 1) {
    arr[i] = arr[i - 1] + arr[i - 2];
  }

  return arr[n - 1];
};
