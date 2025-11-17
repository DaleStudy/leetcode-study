function getSum(a: number, b: number): number {
  while (b !== 0) {
    let carry = (a & b) << 1;

    a = a ^ b;

    b = carry;
  }
  return a;
}
