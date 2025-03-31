/**
 * Source: https://leetcode.com/problems/jump-game/
 * 풀이방법: 그리디로 접근
 *
 * 시간복잡도: O(n) - nums의 요소들을 다 방문할 수 있음
 * 공간복잡도: O(1) - 특정 위치만 기억해둘 필요가 있음
 *
 * 다른 풀이
 * - DFS로 처음에 접근했으나 시간 오버로 인해 Fail
 */

function canJump(nums: number[]): boolean {
  let goal = nums.length - 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    const pos = nums[i];
    if (pos + i >= goal) {
      goal = i;
    }
  }
  return goal === 0;
}
