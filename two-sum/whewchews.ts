/*
 * 아이디어
 * 처음부터 배열을 순회하며 [0,1] [0,2] [0,3] [0, ...], [1,2], [1,3], [1,...] ... [nums.length-2, nums.length-1] 를 돌면서 두 인자의 합이 target이 되는 지점을 찾는다.
 * 순서대로 돌면 최악의 경우 가장 마지막 자리까지 갈 수도 있다.
 * 절대 값이 되지 못하는, 최소 조건을 생각해보자.
 * 주의1:범위가 -10^9 <= nums[i] <= 10^9로 음수값도 있음
 * 주의2: 정렬된 순서가 아님.
 * 값을 Map에 저장해두고 {value: index}, Map에 자신과 더했을때 target이 나오는 value가 있는지 확인
 */
function twoSum(nums: number[], target: number): number[] {
  // SC: O(N)
  const dict = new Map();

  // TC: O(N)
  for (let i = 0; i <= nums.length - 1; i++) {
    const curr = nums[i];
    const pairValue = target - curr;
    if (dict.has(pairValue)) {
      return [dict.get(pairValue), i];
    }

    dict.set(curr, i);
  }
}

// TC: O(N)
// SC: O(N)
