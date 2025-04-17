/**
 * 시간복잡도: O(n)
 *  - for문 O(n)
 * 공간복잡도: O(n)
 *  - arr O(n)
 */
// const climbStairs = (n) => {
//   const arr = [1, 2];

//   for (let i = 2; i < n; i += 1) {
//     arr[i] = arr[i - 1] + arr[i - 2];
//   }

//   return arr[n - 1];
// };

/**
 * 시간복잡도: O(n)
 *  - for문 O(n)
 * 공간복잡도: O(1)
 */
const climbStairs = (n) => {
  let one = 1;
  let two = 1;

  for (let i = 0; i <= n - 2; i += 1) {
    let temp = one + two;
    one = two;
    two = temp;
  }

  return two;
};
