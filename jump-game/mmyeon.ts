/**
 *@link https://leetcode.com/problems/jump-game/description/
 *
 * 접근 방법 :
 *  - 현재 인덱스에서 최대로 도달할 수 있는 인덱스를 갱신하여 마지막 인덱스에 도달할 수 있는지 체크
 *  - 최대 도달할 수 있는 인덱스가 현재 인덱스보다 작으면, 이후는 확인할 필요 없으니까 false 리턴
 *
 * 시간복잡도 : O(n)
 *  - n = 배열의 길이, 배열 1회만 순회
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */

function canJump(nums: number[]): boolean {
  const lastIndex = nums.length - 1;
  let maxReachableIndex = 0;

  for (let i = 0; i < nums.length; i++) {
    if (maxReachableIndex < i) return false;

    maxReachableIndex = Math.max(maxReachableIndex, i + nums[i]);

    if (lastIndex <= maxReachableIndex) return true;
  }

  return false;
}
