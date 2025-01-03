/**
 * 190. Reverse Bits
 * Reverse bits of a given 32 bits unsigned integer.
 *
 * https://leetcode.com/problems/reverse-bits/description/
 */

// O(1) time
// O(1) space
function reverseBits(n: number): number {
  const bits: number[] = [];

  while (bits.length < 32) {
    bits.push(n & 1);
    n = n >> 1;
  }

  let result = 0;
  let scale = 1;
  for (let i = bits.length - 1; i >= 0; i--) {
    result += bits[i] * scale;
    scale *= 2;
  }

  return result;
}
