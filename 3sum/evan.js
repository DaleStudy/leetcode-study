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
