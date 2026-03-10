function topKFrequent(nums: number[], k: number): number[] {
  const count = {} as Record<string, number>;
  for (const num of nums) {
    count[num] = (count[num] || 0) + 1;
  }

  return Object.entries(count)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map(([key]) => Number(key));
}

topKFrequent([1, 1, 1, 2, 2, 3], 2); // [1,2]
topKFrequent([1], 1); // [1]
topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2); // [1,2]
topKFrequent([4, 1, -1, 2, -1, 2, 3], 2); // [2,-1]
