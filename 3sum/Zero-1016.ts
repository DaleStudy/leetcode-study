/**
 * 시간 복잡도 O(n²)
 * 공간 복잡도 O(log n)
 *
 * 접근: 오름차순 정렬 + 투 포인터
 * - 기준 인덱스 i를 고정하고, left = i + 1, right = 끝에서 탐색
 * - 정렬된 상태에서 같은 값을 건너뛰는 방식으로 중복 제거 (Set 불필요)
 */
function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];
  nums.sort((a, b) => a - b); // 오름차순 정렬

  for (let i = 0; i < nums.length - 2; i++) {
    // 기준 숫자가 이전과 같으면 동일한 조합이 나오므로 건너뜀
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    // 최적화: 기준 숫자가 양수면 뒤의 숫자들도 모두 양수 → 합이 0 불가능
    if (nums[i] > 0) break;

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === 0) {
        result.push([nums[i], nums[left], nums[right]]);

        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;

        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }

  return result;
}
