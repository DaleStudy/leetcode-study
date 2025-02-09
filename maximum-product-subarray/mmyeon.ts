/**
 * @link https://leetcode.com/problems/maximum-product-subarray/
 *
 * 접근 방법 :
 *  - 음수가 짝수번 나오면 최대값이 될 수 있으니까 최소곱, 최대곱을 모두 업데이트
 *  - 현재 값이 단독으로 최소, 최대일 수 있으니까 현재값, 최소곱 * 현재값, 최대곱 * 현재값을 비교
 *
 * 시간복잡도 : O(n)
 *  - nums 1회 순회
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */
function maxProduct(nums: number[]): number {
  let currentMin = nums[0],
    currentMax = nums[0],
    maxSoFar = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];
    const minCandidate = currentMin * num;
    const maxCandidate = currentMax * num;

    currentMin = Math.min(num, minCandidate, maxCandidate);
    currentMax = Math.max(num, minCandidate, maxCandidate);

    maxSoFar = Math.max(currentMax, maxSoFar);
  }

  return maxSoFar;
}
