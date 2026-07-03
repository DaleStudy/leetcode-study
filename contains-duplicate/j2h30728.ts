/**
 * @param {number[]} nums
 * @return {boolean}
 * @description
 * - 시간 복잡도: 평균 O(n), 중복 조기 발견 시 최선 O(1)
 * - 공간 복잡도: 최악 O(n)
 */
function containsDuplicate(nums: number[]): boolean {
  const set = new Set();

  for (const num of nums) {
    if (set.has(num)) {
      return true;
    }
    set.add(num);
  }
  return false;
}

/**
 * @param {number[]} nums
 * @return {boolean}
 * @description
 * - 시간 복잡도: 항상 O(n) - new Set(nums): 원소 n개를 모두 삽입하므로 평균 O(n)
 * - 공간 복잡도: O(n)
 */
function containsDuplicate(nums: number[]): boolean {
  const set = new Set(nums);
  const hasDuplicate = set.size !== nums.length;
  return hasDuplicate;
}
