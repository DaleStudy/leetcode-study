var longestConsecutive = function (nums) {
  const Set = new Set(nums);
  let maxLength = 0;

  for (let num of Set) {
    if (!Set.has(num - 1)) {
      let currentNum = num;
      let count = 1;

      // 연속된 숫자 탐색
      while (Set.has(currentNum + 1)) {
        currentNum++;
        count++;
      }

      maxLen = Math.max(maxLength, count);
    }
  }

  return maxLength;
};
