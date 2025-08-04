function hammingWeight(n: number): number {
  const RADIX = 2;

  return n.toString(RADIX).match(/1/g)?.length || 0;
}
