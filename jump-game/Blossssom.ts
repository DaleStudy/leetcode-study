/**
 * @pseudocode
 * - 해당 칸에서 가장 멀리 갈 수 있는 값
 * - 각 nums의 요소 반복
 *  - 가장 멀리 갈 수 있는 값 업데이트
 *  - if 가장 멀리 갈 수 있는 값이 현재 idx보다 작다면
 *      - false
 *  - if 가장 멀리 갈 수 있는 값이 nums의 마지막 idx보다 크거나 같다면
 *      - true
 * @param nums - 정수 배열
 * @returns - 마지막 요소까지 접근이 가능한지 반환
 */

function canJump(nums: number[]): boolean {
  let maxReach = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > maxReach) {
      return false;
    }

    maxReach = Math.max(maxReach, i + nums[i]);

    if (maxReach >= nums.length - 1) {
      return true;
    }
  }

  return true;
}

const nums = [2, 3, 1, 1, 4];
canJump(nums);


