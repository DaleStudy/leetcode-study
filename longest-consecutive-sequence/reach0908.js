/**
 * @description
 * time complexity: O(n log n)
 * space complexity: O(n)
 * runtime: 57ms
 * 풀이 방법: 중복을 제거하고 정렬한 다음에 연속된 숫자의 개수를 카운트하여 최대값을 반환한다.
 * @param {number[]} nums
 * @return {number}
 */
const longestConsecutive = function (nums) {
  if (nums.length === 0) return 0;
  const sortedNums = [...new Set(nums)].sort((a, b) => a - b);

  let maxConsecutiveCount = 1;
  let currentConsecutiveCount = 1;

  for (let i = 1; i < sortedNums.length; i += 1) {
    if (sortedNums[i] === sortedNums[i - 1] + 1) {
      currentConsecutiveCount += 1;
    } else {
      currentConsecutiveCount = 1;
    }

    maxConsecutiveCount = Math.max(
      maxConsecutiveCount,
      currentConsecutiveCount
    );
  }

  return maxConsecutiveCount;
};
