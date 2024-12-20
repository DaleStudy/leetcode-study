function topKFrequent(nums: number[], k: number): number[] {
  const frequency = nums.reduce(
    (acc, n) => acc.set(n, (acc.get(n) ?? 0) + 1),
    new Map<number, number>()
  );

  return Array.from(frequency)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((item) => item[0]);
}
