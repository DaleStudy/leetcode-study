function hammingWeight(n: number): number {
  return n
    .toString(2)
    .split("")
    .reduce((acc, i) => acc + +i, 0);
}
