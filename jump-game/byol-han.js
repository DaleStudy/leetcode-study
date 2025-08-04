/**
 * https://leetcode.com/problems/jump-game/description/
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let maxReach = 0; // 현재까지 도달할 수 있는 최대 인덱스

  for (let i = 0; i < nums.length; i++) {
    // 현재 위치가 도달 가능한 최대 거리보다 멀다면 끝에 도달할 수 없음
    if (i > maxReach) {
      return false;
    }

    // 현재 위치에서 갈 수 있는 최대 위치 업데이트
    maxReach = Math.max(maxReach, i + nums[i]);

    // 최종 목적지에 도달 가능하면 true 바로 반환
    if (maxReach >= nums.length - 1) {
      return true;
    }
  }

  // 반복문 끝나도 못 도달한 경우
  return false;
};
