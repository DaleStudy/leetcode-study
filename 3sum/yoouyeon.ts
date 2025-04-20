// [15] 3Sum

/**
 * 앞서 시도한 방법들
 * - DFS로 모든 조합을 구하는 방법 : Time Limit Exceeded...
 * - Two Sum에서 풀었던 방법대로 Set을 이용해서 조합을 만드는 방법 : Time Limit Exceeded...
 */

/**
 * [Idea]
 * Two Pointers
 * Set을 이용하지 않고 정렬을 통해서 중복된 조합을 제거하는 방법
 * 투포인터 방식으로 x를 고정하고 y, z를 찾는다.
 * 중복된 원소는 건너뛰는 방식으로 중복된 조합을 제거한다.
 *
 * [Time Complexity]
 * O(n^2) (n: nums의 원소 개수)
 * 시작 원소 (idx)를 고정시켜 nums를 순회하는 데 O(n) 소요되고
 * 내부에서 투포인터로 y, z를 찾는 데 O(n) 소요되므로 O(n^2)
 *
 * [Space Complexity]
 * O(1)
 * left, right 변수만 사용하므로 O(1)
 */
function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];
  nums.sort((a, b) => a - b);

  for (let idx = 0; idx < nums.length - 2; idx++) {
    // 같은 숫자로 시작하는 조합을 제거 (시도하지 않는다)
    if (idx > 0 && nums[idx] === nums[idx - 1]) continue;

    let left = idx + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[idx] + nums[left] + nums[right];

      if (sum === 0) {
        result.push([nums[idx], nums[left], nums[right]]);
        // 중복된 조합을 제거하기 위해서 같은 원소인 경우를 건너뛴다.
        while (left < right && nums[left] === nums[left + 1]) {
          left++;
        }
        while (left < right && nums[right] === nums[right - 1]) {
          right--;
        }
        // 다음 조합을 시도하기
        left++;
        right--;
        continue;
      }
      if (sum < 0) {
        left++;
        continue;
      }
      right--;
    }
  }

  return result;
}
