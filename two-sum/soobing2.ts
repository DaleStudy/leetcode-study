/**
 * 문제 유형
 * - Array
 *
 * 문제 설명
 * - 주어진 배열에서 두 수를 더해서 target 값이 되는 인덱스를 반환
 *
 * 아이디어
 * - 순회하면서 map을 먼저 만들어두고, 다시 순회하면서 target-nums[i] 값이 있는지 확인
 */
function twoSum(nums: number[], target: number): number[] {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    map.set(nums[i], i);
  }

  for (let i = 0; i < nums.length; i++) {
    const index = map.get(target - nums[i]);
    if (i === index || index === undefined) continue;

    return [i, index];
  }

  return [];
}
