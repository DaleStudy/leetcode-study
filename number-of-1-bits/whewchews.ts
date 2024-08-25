function hammingWeight(n: number): number {
  // SC: log(1)
  let val = 0;
  while (n > 0) {
    val += n % 2;

    // TC: log₂(n)
    n = Math.floor(n / 2);
  }

  return val;
}

// TC: O(log N)
// SC: O(1)
