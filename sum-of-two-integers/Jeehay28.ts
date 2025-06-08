// TC: O(1)
// SC: O(1)
function getSum(a: number, b: number): number {
  while (b !== 0) {
    let carry = a & b;
    a = a ^ b; // sum WITHOUT the carry
    b = carry << 1; // new carry
  }

  return a;
}

