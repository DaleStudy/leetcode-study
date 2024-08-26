// TC: O(N)
// SC: O(N)

/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
  const result = [0];
  let pointer = 0;
  let lastPointer = 0;

  for (let num = 1; num <= n; num++) {
    result.push(result[pointer] + 1);

    if (pointer === lastPointer) {
      lastPointer = result.length - 1;
      pointer = 0;
    } else {
      pointer += 1;
    }
  }

  return result;
};
