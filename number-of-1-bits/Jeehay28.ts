// Approach 2
// 🗓️ 2025-04-15
// ⏳ Time Complexity: O(log n)
// 💾 Space Complexity: O(1)

function hammingWeight(n: number): number {
  // n(이진수) & 1 -> 1: 이진수 n의 마지막 비트가 1인 경우에만 1 반환
  // n(이진수) >> 1: 마지막 비트 제거
  // 🔍 In binary numbers:
  // Decimal: 11
  // Binary:  1   0   1   1
  //          ↑           ↑
  //         MSB         LSB
  //     (Most Sig.)   (Least Sig.)
  // n & 1: only checks the least significant bit (LSB), if the LSB is 1, the result is 1.
  // n >>= 1: Each bit is moved one place to the right.

  let count = 0;

  while (n) {
    count += n & 1; // add 1 if the least significant bit of n is 1
    n >>= 1; // The LSB is removed (dropped).
  }

  return count;
}


// Approach 1
// 🗓️ 2025-04-15
// ⏳ Time Complexity: O(log n)
// 💾 Space Complexity: O(1)

// function hammingWeight(n: number): number {
//   // input: a positive number n
//   // output: the number of set bits in binary representation
//   // set bits: a bit in the binary representaton of a number that has a value of 1
//   // 11 -> 1011 -> 3

//   let cnt = 0;
//   while (n > 0) {
//     if (n % 2 === 1) {
//       cnt += 1;
//     }
//     n = Math.floor(n / 2);
//   }

//   return cnt;
// }

