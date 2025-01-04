/**
 * Runtime: 19ms, Memory: 52.48MB
 *
 * 접근
 * 직관적으로 생각했을 때, 0부터 n까지의 숫자 중에서 없는 숫자를 찾아야 한다.
 * 완전 탐색으로 정렬한 배열에서 순서대로 비교하면서 없는 숫자를 찾을 수 있다.
 * Time Complexity: O(nlogn)
 * Space Complexity: O(n)
 *
 * Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
 */

function missingNumber(nums: number[]): number {
  const numsLen = nums.length;
  const sortedNums = nums.sort((a, b) => a - b); // 오름차순 정렬

  for (let i = 0; i <= numsLen; i++) {
    if (i !== sortedNums[i]) {
      return i;
    }
  }
}

/**
 * Runtime: 1ms, Memory: 51.96MB
 *
 * 접근
 * Follow up에 대한 해결 방법
 * 0부터 n까지의 숫자의 합을 구한 뒤, 주어진 배열의 합을 빼면 없는 숫자를 찾을 수 있다.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

function missingNumber(nums: number[]): number {
  const size = nums.length;
  const sum = (size * (size + 1)) / 2;
  const accurate = nums.reduce((sum, num) => sum + num, 0);

  return sum - accurate;
}
