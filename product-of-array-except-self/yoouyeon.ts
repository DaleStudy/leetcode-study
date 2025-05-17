// [238] Product of Array Except Self

/**
 * [Idea]
 * nums[i] 를 기준으로 왼쪽 부분 (prefix)은 계속 구간을 늘려주고, 오른쪽 부분(suffix)은 계속 구간을 줄여주는 방식
 * i = 0:
 *      [ ] * [2, 3, 4, 5, 6] => prefix: 0, suffix: 2 * 3 * 4 * 5 * 6
 * i = 1:
 *      [1] * [3, 4, 5, 6] => prefix: 1, suffix: 3 * 4 * 5 * 6
 * i = 2:
 *      [1, 2] * [4, 5, 6] => prefix: 1 * 2, suffix: 4 * 5 * 6
 * i = 3:
 *      [1, 2, 3] * [5, 6] => prefix: 1 * 2 * 3, suffix: 5 * 6
 *
 * [Time Complexity]
 * O(n) (n: nums의 길이)
 * 1. prefix를 구하는 과정에서 O(n)
 * 2. suffix를 구하는 과정에서 O(n)
 *
 * [Space Complexity]
 * O(1)
 * answer 배열을 제외한 추가적인 공간을 사용하지 않음
 *
 */
function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const answer = new Array<number>(nums.length);

  // answer 배열에 prefix값 설정해주기
  let prefix = 1;
  for (let idx = 0; idx < n; idx++) {
    answer[idx] = prefix;
    prefix *= nums[idx];
  }

  // 각 prefix에 suffix 값 누적해서 곱해주기
  let suffix = 1;
  for (let idx = n - 1; idx >= 0; idx--) {
    answer[idx] *= suffix;
    suffix *= nums[idx];
  }

  return answer;
}
