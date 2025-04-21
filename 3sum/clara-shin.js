/**
 * 배열에서 합이 0이 되는 세 숫자를 찾기
 *
 * 요구사항 & 제약조건:
 * 세 개의 다른 인덱스에 있는 숫자들의 합이 0이 되어야 함
 * 결과에 중복된 조합이 없어야 함
 * 배열 크기는 3에서 3000까지
 * 배열 요소는 -10^5부터 10^5까지의 정수
 *
 * 접근방법:
 * 1. 브루트포스(이중for문, 완전탐색) - O(n^3) 시간복잡도
 * 2. 정렬 후 투 포인터 - O(n^2) 시간복잡도 ✅
 *
 * 배열을 정렬 후, 배열을 순회하며 각 요소를 첫 번째 숫자로 고정
 * 고정된 숫자 다음부터 ~ 배열 끝까지 투 포인터를 사용 ➡️ 나머지 두 수의 합이 첫 번째 수의 음수가 되는 조합 찾기
 * 중복을 피하기 위해 같은 값을 가진 연속된 요소는 스킵
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const result = [];
  const n = nums.length;

  if (n < 3) return result;

  nums.sort((a, b) => a - b); // 오름차순 정렬

  if (nums[0] > 0 || nums[n - 1] < 0) return result;

  // 배열을 순회하며 첫 번째 숫자 고정
  for (let i = 0; i < n - 2; i++) {
    // 중복된 값 건너뛰기 (첫 번째 숫자)
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    // 첫 번째 숫자가 양수면 for문 탈출
    if (nums[i] > 0) break;

    // 현재 숫자와 가장 작은 두 숫자의 합 > 0 => 탈출
    if (nums[i] + nums[i + 1] + nums[i + 2] > 0) break;

    // 현재 숫자와 가장 큰 두 숫자의 합 < 0 => 건너뛰기
    if (nums[i] + nums[n - 2] + nums[n - 1] < 0) continue;

    // 두 번째, 세 번째 숫자를 찾기 위한 투 포인터
    let left = i + 1;
    let right = n - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum < 0) {
        // 합이 0보다 작으면 left 포인터를 오른쪽으로 이동
        left++;
      } else if (sum > 0) {
        // 합이 0보다 크면 right 포인터를 왼쪽으로 이동
        right--;
      } else {
        // 합이 0이면 결과에 추가
        result.push([nums[i], nums[left], nums[right]]);

        // 중복된 값 건너뛰기 (두 번째, 세 번째 숫자)
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;

        // 다음 조합을 찾기 위해 포인터 이동
        left++;
        right--;
      }
    }
  }

  return result;
};
