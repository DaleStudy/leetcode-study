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

/**
 * @description
 * time complexity: O(n)
 * space complexity: O(n)
 * runtime: 36ms
 * 풀이 방법: 중복을 제거하고 Set을 사용하여 O(1) 조회 가능하도록 한 다음에 연속된 숫자의 개수를 카운트하여 최대값을 반환한다.
 * @param {number[]} nums
 * @return {number}
 */
const longestConsecutive2 = function (nums) {
  if (nums.length === 0) return 0;

  // Set을 사용하여 O(1) 조회 가능
  const numSet = new Set(nums);
  let maxLength = 0;

  for (const num of numSet) {
    // 현재 숫자가 연속 수열의 시작점인지 확인
    // num-1이 존재하지 않으면 num이 시작점
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;

      // 연속된 다음 숫자들이 존재하는 동안 계속 탐색
      while (numSet.has(currentNum + 1)) {
        currentNum += 1;
        currentLength += 1;
      }

      // 최대 길이 업데이트
      maxLength = Math.max(maxLength, currentLength);
    }
  }

  return maxLength;
};
