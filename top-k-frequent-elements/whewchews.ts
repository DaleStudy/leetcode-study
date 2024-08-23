function topKFrequent(nums: number[], k: number): number[] {
  const dict: Map<number, number> = new Map();

  // TC: O(N)
  // SC: O(N)
  nums.forEach((n) => {
    if (!dict.has(n)) dict.set(n, 1);
    else {
      dict.set(n, dict.get(n) + 1);
    }
  });

  // TC: O(N)
  // SC: O(N)
  const buckets: number[][] = Array(nums.length + 1)
    .fill(0)
    .map((_) => []);
  Array.from(dict.entries()).forEach(([num, cnt]) => {
    buckets[cnt].push(num);
  });

  // TC: O(N) + O(k) = O(N)
  // SC: O(N)
  return buckets.flat().slice(-k);
}

// TC: O(N)
// SC: O(N)
