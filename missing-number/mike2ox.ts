/**
 * source: https://leetcode.com/problems/missing-number/
 * 풀이방법: 0부터 n까지의 합에서 주어진 배열의 합을 빼면 빠진 숫자를 구할 수 있음
 *
 * 시간복잡도: O(n) (n: nums의 길이)
 * 공간복잡도: O(1) (상수 공간만 사용)
 */

function missingNumber(nums: number[]): number {
  const n = nums.length;
  let expectedSum = (n * (n + 1)) / 2; // 0부터 n까지의 합 공식
  let realSum = nums.reduce((sum, cur) => sum + cur, 0);

  return expectedSum - realSum;
}
