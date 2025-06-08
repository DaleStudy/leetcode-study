/**
 * 문제 해설
 * - 현재 위치에서 최대 점프할 수 있는 갯수를 담고 있는 배열, 마지막 항목에 도달이 가능한지 반환하는 문제
 *
 * 아이디어
 * 1) 그리디 알고리즘
 * - 배열을 쭉 순회하면서 다음 이동 가능한 횟수를 비교하여 다음 항목으로 이동이 가능한지 체크, 없다면 false 반환.
 * - 일단 현재까지 왔다면 이후에 최대로 갈 수 있는 값을 업데이트.
 */
function canJump(nums: number[]): boolean {
  let reachable = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > reachable) return false;
    reachable = Math.max(reachable, i + nums[i]);
  }
  return true;
}
