/**
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 * 중복된 숫자 제거, 정렬을 한 이후, 하나씩 순회하면서 연속된 숫자중 가장 긴 것을 찾는다.
 */

function longestConsecutiveWithSort(nums: number[]): number {
  const sortNums = [...new Set(nums)].sort((a, b) => a - b);

  let maxConsecutiveElementsCount = 0;

  let currentConsecutiveElementsCount = 0;
  let prevNumber: number | undefined = undefined;

  for (let i = 0; i < sortNums.length; i++) {
    const currentNumber = sortNums[i];
    if (currentNumber === (prevNumber ?? 0) + 1) {
      currentConsecutiveElementsCount++;
      maxConsecutiveElementsCount = Math.max(
        maxConsecutiveElementsCount,
        currentConsecutiveElementsCount,
      );
    } else {
      currentConsecutiveElementsCount = 1;
    }
    prevNumber = currentNumber;
  }

  maxConsecutiveElementsCount = Math.max(
    maxConsecutiveElementsCount,
    currentConsecutiveElementsCount,
  );

  return maxConsecutiveElementsCount;
}

/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * 중복된 숫자 제거, 집합을 사용하여 하나씩 순회하면서 연속된 숫자중 가장 긴 것을 찾는다.
 */
function longestConsecutiveWithSet(nums: number[]): number {
  const numSet = new Set(nums);

  let maxConsecutiveElementsCount = 0;

  for (const number of numSet) {
    if (!numSet.has(number - 1)) {
      let currentNumber = number;
      let currentConsecutiveElementsCount = 1;

      while (numSet.has(currentNumber + 1)) {
        currentNumber++;
        currentConsecutiveElementsCount++;
      }

      maxConsecutiveElementsCount = Math.max(
        maxConsecutiveElementsCount,
        currentConsecutiveElementsCount,
      );
    }
  }

  return maxConsecutiveElementsCount;
}
