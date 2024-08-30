// T.C. O(n)
// S.C. O(n)
function twoSum(nums: number[], target: number): number[] {
  const sumMap = new Map<number, number>();
  for (const [i, num] of nums.entries()) {
    const diff = target - num;
    if (sumMap.has(diff)) {
      return [sumMap.get(diff)!, i];
    }
    sumMap.set(num, i);
  }
  return [];
}
