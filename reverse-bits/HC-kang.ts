/**
 * https://leetcode.com/problems/reverse-bits
 * T.C. O(1)
 * S.C. O(1)
 */
function reverseBits(n: number): number {
  let result = 0;
  for (let i = 0; i < 32; i++) {
    result = (result << 1) | (n & 1);
    n >>= 1;
  }
  return result >>> 0;
}
