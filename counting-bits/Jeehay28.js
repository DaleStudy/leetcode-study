// ✅ Time Complexity: O(n)
// ✅ Space Complexity: O(n)

/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
  // dp[i] = 1 + dp[i - MSB]
  // MSB(Most Significant Bit)

  let dp = new Array(n + 1).fill(0);
  let msb = 1;

  for (let i = 1; i <= n; i++) {
    if (msb * 2 === i) {
      msb = i;
    }

    dp[i] = 1 + dp[i - msb];
  }

  return dp;
};

// ✅ Time Complexity: O(n * logn)
// ✅ Space Complexity: O(n)

/**
 * @param {number} n
 * @return {number[]}
 */
// var countBits = function (n) {
//   let result = [0];
//   const count = (num) => {
//     let cnt = 0;
//     while (num !== 0) {
//       cnt += num % 2;
//       num = Math.floor(num / 2);
//     }
//     return cnt;
//   };

//   for (let i = 1; i <= n; i++) {
//     const temp = count(i);
//     result.push(temp);
//   }

//   return result;
// };

