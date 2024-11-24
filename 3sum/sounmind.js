/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const sorted = nums.sort((a, b) => a - b);
  const result = [];

  for (let i = 0; i < sorted.length; i++) {
    const fixedNumber = sorted[i];
    const previousFixedNumber = sorted[i - 1];

    if (fixedNumber === previousFixedNumber) {
      continue;
    }

    let [leftEnd, rightEnd] = [i + 1, sorted.length - 1];

    while (leftEnd < rightEnd) {
      const sum = fixedNumber + sorted[leftEnd] + sorted[rightEnd];

      if (sum === 0) {
        result.push([sorted[leftEnd], sorted[rightEnd], sorted[i]]);

        while (
          sorted[leftEnd + 1] === sorted[leftEnd] ||
          sorted[rightEnd - 1] === sorted[rightEnd]
        ) {
          if (sorted[leftEnd + 1] === sorted[leftEnd]) {
            leftEnd += 1;
          }

          if (sorted[rightEnd - 1] === sorted[rightEnd]) {
            rightEnd -= 1;
          }
        }

        leftEnd += 1;
        rightEnd -= 1;
      } else if (sum < 0) {
        leftEnd += 1;
      } else {
        rightEnd -= 1;
      }
    }
  }

  return result;
};

/**
 * Time Complexity: O(n^2)
 * The algorithm involves sorting the input array, which takes O(n log n) time.
 * The main part of the algorithm consists of a loop that runs O(n) times, and within that loop, there is a two-pointer technique that runs in O(n) time.
 * Thus, the overall time complexity is O(n log n) + O(n^2), which simplifies to O(n^2).
 *
 * Space Complexity: O(n)
 * The space complexity is O(n) due to the space needed for the sorted array and the result array.
 * Although the sorting algorithm may require additional space, typically O(log n) for the in-place sort in JavaScript, the dominant term is O(n) for the result storage.
 */
