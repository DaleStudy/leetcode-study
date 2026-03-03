function containsDuplicate(nums: number[]): boolean {
  const numsMap = new Map();
  nums.forEach(n => {
    numsMap.set(n, (numsMap.get(n) || 0) + 1);
  });

  for (const [_, count] of numsMap) {
    if (count >= 2) return true;
  }

  return false;
}
