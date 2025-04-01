// 1번째 풀이 (hashMap)
function containsDuplicate1(nums: number[]): boolean {
  const seen: Record<number, boolean> = {};

  const isDuplicate = nums.some((num) => {
    if (seen[num]) return true;
    seen[num] = true;
    return false;
  });

  return isDuplicate;
}

// 2번째 풀이(Set)
function containsDuplicate2(nums: number[]): boolean {
  const set = new Set();

  for (const num of nums) {
    if (set.has(num)) {
      return true;
    }
    set.add(num);
  }

  return false;
}
