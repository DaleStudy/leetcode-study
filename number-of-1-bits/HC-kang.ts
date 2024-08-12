/**
191. Number of 1 Bits

Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
 */

function hammingWeight(n: number): number {
  // Time complexity: O(logn)
  // Space complexity: O(logn)
  // it has a better readability and not so bad in space complexity
  return n.toString(2).split('1').length - 1;

  // Time complexity: O(logn)
  // Space complexity: O(1)
  // it's better in space complexity, but sometimes the bitwise operation is not easy to understand
  let count = 0;
  while (n !== 0) {
    count += n & 1;
    n >>>= 1;
  }
  return count;
}
