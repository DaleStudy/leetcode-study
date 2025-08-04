function topKFrequent(nums: number[], k: number): number[] {
  const map: Map<number, number> = new Map();

  nums.forEach((val) => {
    if (map.has(val)) map.set(val, map.get(val)!! + 1);
    else map.set(val, 1);
  });

  return Array.from(map)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((item) => item[0]);
}
