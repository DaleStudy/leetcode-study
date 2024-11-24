/**
 * @param {number[]} heights
 * @return {number}
 */
var maxArea = function (heights) {
  let maxAmount = 0;
  let [leftEnd, rightEnd] = [0, heights.length - 1];

  while (leftEnd < rightEnd) {
    const minHeight = Math.min(heights[leftEnd], heights[rightEnd]);
    const horizontalLength = rightEnd - leftEnd;

    maxAmount = Math.max(maxAmount, minHeight * horizontalLength);

    if (heights[leftEnd] > heights[rightEnd]) {
      rightEnd -= 1;
    } else {
      leftEnd += 1;
    }
  }

  return maxAmount;
};
