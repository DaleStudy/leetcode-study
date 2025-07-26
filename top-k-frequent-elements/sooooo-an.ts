function topKFrequent(nums: number[], k: number): number[] {
  const frequentMap = new Map<number, number>();

  for (const num of nums) {
    frequentMap.set(num, (frequentMap.get(num) ?? 0) + 1);
  }

  const sorted = Array.from(frequentMap.entries()).sort((a, b) => b[1] - a[1]);

  return sorted.slice(0, k).map(([key]) => Number(key));
}

/**
 * Runtime 9ms / 78.90%
 * Memory 60.130MB / 66.67%
 */
