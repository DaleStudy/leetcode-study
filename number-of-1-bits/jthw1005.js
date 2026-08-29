function hammingWeight(n) {
  return n
    .toString(2)
    .split('')
    .filter((v) => v === '1').length;
}
