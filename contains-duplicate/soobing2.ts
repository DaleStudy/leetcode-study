/**
 * 문제 유형
 * - Array
 *
 * 문제 설명
 * - 중복된 수가 있는 경우 true, 없으면 false 반환
 *
 * 아이디어
 * - 전체적으로 순회하면서 중복된 수가 있는지 확인
 *
 */
function containsDuplicate(nums: number[]): boolean {
  const set = new Set<number>();
  for (let i = 0; i < nums.length; i++) {
    if (set.has(nums[i])) return true;

    set.add(nums[i]);
  }
  return false;
}
