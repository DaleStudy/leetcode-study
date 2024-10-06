/**
 * https://leetcode.com/problems/sum-of-two-integers
 * T.C. O(log a)
 * S.C. O(1)
 */
function getSum(a: number, b: number): number {
  while (b != 0) {
    let carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
}
