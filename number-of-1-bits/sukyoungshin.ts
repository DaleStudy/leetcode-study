function hammingWeight(n: number): number {
  let count = 0;
  let num = n;

  while (num > 0) {
    if (num % 2 === 1) {
      count++;
    }
    num = Math.floor(num / 2);
  }

  return count;
};
