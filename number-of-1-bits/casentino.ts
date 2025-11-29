function hammingWeight(n: number): number {
  let num = n;
  let output = 0;
  while (num !== 1) {
    if (num % 2 === 1) {
      output += 1;
      num = (num - 1) / 2;
    } else {
      num = num / 2;
    }
  }
  if (num === 1) {
    output += 1;
  }
  return output;
}
