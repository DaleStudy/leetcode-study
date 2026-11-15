// 시간 복잡도: O(n log n)
// 공간 복잡도: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  let cnt = 0;
  const set = new Set(nums);
  const sortArray = Array.from(set).sort((a, b) => a - b);
  const cntArray = [];

  for (let i = 0; i < sortArray.length; i++) {
    if (sortArray[i] + 1 !== sortArray[i + 1]) {
      cntArray.push(cnt + 1);
      cnt = 0;
    } else {
      cnt += 1;
    }
  }

  if (nums.length === 0) return 0;
  else return Math.max(...cntArray);
};
