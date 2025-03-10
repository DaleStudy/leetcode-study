/**
 *@link https://leetcode.com/problems/house-robber-ii/description/
 *
 * 접근 방법 :
 *  - DP를 활용해서 현재 위치까지의 최대값을 업데이트
 *  - 원형 구조로 첫 번째 집과 마지막 집이 둘다 포함될 수 없기 때문에, 첫 번째 집만 포함하는 경우와 첫 번째 집을 제외하는 경우를 나눠서 계산하고 최대값 비교
 *
 * 시간복잡도 : O(n)
 *  - n = numbs 배열의 길이,  n번 반복하면서 최대값 계산
 *
 * 공간복잡도 : O(1)
 *  - dp 배열을 사용하는 대신 고정된 배열(prev, doublePrev)을 사용
 */
const calculateMaxMoney = (houses: number[]) => {
  let prev = 0;
  let doublePrev = 0;

  for (let i = 0; i < houses.length; i++) {
    const current = Math.max(prev, doublePrev + houses[i]);

    doublePrev = prev;
    prev = current;
  }

  return prev;
};

function rob(nums: number[]): number {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  const robWithFirstHouse = calculateMaxMoney(nums.slice(0, nums.length - 1));
  const robWithoutFirstHouse = calculateMaxMoney(nums.slice(1, nums.length));

  return Math.max(robWithFirstHouse, robWithoutFirstHouse);
}
