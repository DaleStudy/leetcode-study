/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let farthest = 0;

  for (let i = 0; i < nums.length; i++) {
    // 현재 위치가 지금까지 갈 수 있는 가장 먼 거리보다 멀다면
    if (i > farthest) {
      return false; // 도달 불가능
    }

    // 현재 위치에서 갈 수 있는 가장 먼 거리 업데이트
    farthest = Math.max(farthest, i + nums[i]);
  }

  return true;
};
