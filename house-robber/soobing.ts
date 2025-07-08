/**
 * 문제 설명
 * - 주어진 배열의 시작과 끝이 연결되어 있는 원형이라고 할 경우에, 이웃하는 집은 털 수 없고 최대로 털 수 있는 돈을 구하는 문제
 *
 * 아이디어
 * 1) 동적 계획법(Dynamic Programming) 활용
 *   - 원형 구조이므로 첫번째 집과 마지막집은 동시에 털 수 없음
 *   - 따라서 두 가지 경우로 나누어 계산하고, 두 결과 중 더 큰 값을 반환
 * 2) 선형 배열에 대한 최대 금액 계산
 *   - 매 순회마다 현재 집을 털 경우(prev2 + num)와 털지 않을 경우(prev1) 중 큰 값을 선택
 *   - 최종적으로 prev1에 최대값이 저장
 */
function robLinear(nums: number[]) {
  let prev1 = 0;
  let prev2 = 0;

  for (const num of nums) {
    const temp = prev1;
    prev1 = Math.max(prev2 + num, prev1);
    prev2 = temp;
  }

  return prev1;
}

function rob(nums: number[]): number {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  const temp1 = robLinear(nums.slice(0, nums.length - 1));
  const temp2 = robLinear(nums.slice(1));

  return Math.max(temp1, temp2);
}
