// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  let answer = 0;
  const consecutiveDict = new Map();

  for (const num of nums) {
    consecutiveDict.set(num, true);
  }

  for (const num of nums) {
    if (consecutiveDict.has(num - 1)) {
      continue;
    }

    let length = 1;
    while (consecutiveDict.has(num + length)) {
      length++;
    }

    answer = Math.max(answer, length);
  }

  return answer;
};
