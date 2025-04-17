function longestConsecutive(nums: number[]): number {
  const set = new Set<number>(nums);
  let result = 0;

  for (const num of set) {
    if (set.has(num - 1)) continue;
    let length = 1;
    while (set.has(num + length)) length++;
    result = Math.max(length, result);
  }

  return result;
}
