/**
 * 주어진 배열에서 두 숫자의 합이 target이 되는 idx 쌍을 반환하는 함수
 * - 시간 복잡도: O(n)
 *   - 한번의 배열을 순회하며 Map에 값을 저장하고, Map에서 값을 찾음
 * - 공간 복잡도: O(n)
 *  - 숫자와 그때의 idx를 쌍으로하는 Map
 * 
 * @param {number[]} nums  - 숫자 배열
 * @param {number} target - 타겟 합
 * @returns {number[]} - 합을 만들 수 있는 idx 배열
 */
function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    const cur = nums[i]; // 현재 값
    const reamin = target - cur; // 나머지
    if (map.has(reamin)) {
        // Non-null assertion operator(!)를 사용하여 undefined가 아님을 단언
      return [map.get(reamin)!, i];
    }
    // 나머지를 찾지 못한 경우 현재 값을 저장
    map.set(cur, i);
  }
  return []; // 목표 합을 만들 수 있는 숫자가 없는 경우 빈 배열 반환
}
