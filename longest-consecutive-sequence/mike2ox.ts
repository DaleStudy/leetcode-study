/**
 * Source: https://leetcode.com/problems/longest-consecutive-sequence/
 * 풀이방법: 정렬 후 순회를 통해 연속된 값이 있는지 확인
 * 시간복잡도: O(nlogn)
 * 공간복잡도: O(1)
 *
 * 생각나는 풀이방법
 */

function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) return 0;
  const sorted = nums.sort((a, b) => a - b);
  let prev = sorted[0];
  let result = 1;
  let candiResult = 1;

  for (let current of sorted) {
    if (prev === current) continue;
    if (current === prev + 1) {
      candiResult += 1;
    } else {
      if (candiResult > result) {
        result = candiResult;
      }
      candiResult = 1;
    }
    prev = current;
  }

  if (candiResult > result) result = candiResult;
  return result;
}
