/**
 *
 * 접근 방법 :
 *  - 연속되는 숫자 중 빠진 숫자 찾는 거니까 배열 인덱스를 활용하자.
 *  - 배열 요소 순회하면서 map에 요소를 키로 넣고, nums 길이만큼 순회하면서 map에 값 있는지 체크
 *  - 없으면 해당 인덱스 리턴하고, 순회 끝나면 nums 길이 리턴
 *
 * 시간복잡도 : O(n)
 *  - nums 길이만큼 map에 요소 넣고, map에 요소 있는지 체크하니까 O(n)
 *
 * 공간복잡도 : O(n)
 *  - map에 nums 길이만큼 저장하니까 O(n)
 */

function missingNumber(nums: number[]): number {
  const set = new Set(nums);

  for (let i = 0; i < nums.length; i++) {
    if (!set.has(i)) return i;
  }

  return nums.length;
}

// 공간복잡도 O(1) 개선 방법
// - 0부터 n까지의 합 구하고, 실제 nums 요소 값 빼서 빠진 숫자 구함
function missingNumber(nums: number[]): number {
  let sum = 0;

  for (let i = 0; i <= nums.length; i++) {
    sum += i;
    if (i < nums.length) sum -= nums[i];
  }

  return sum;
}
