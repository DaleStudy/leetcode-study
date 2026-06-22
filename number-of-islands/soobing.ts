function hammingWeight(n: number): number {
  let count = 0;
  for(let i = 31; i >= 0; i--) {
      if((n >> i) & 1) {
          count++;
      }
  }
  return count;
};
