// 1번풀이
function longestConsecutive2(nums: number[]): number {
  if (nums.length === 0) return 0;

  const copiedNums = [...new Set(nums)].sort((a, b) => a - b);

  let max = 1; // 지금까지 나왔던 가장 긴 연속 수열의 길이
  let count = 1; // 현재 연속 수열의 길이

  for (let i = 1; i < copiedNums.length; i++) {
    const prev = copiedNums[i - 1];
    const current = copiedNums[i];

    if (current === prev + 1) {
      count++;
      max = Math.max(max, count);
    } else {
      count = 1;
    }
  }

  return max;
};

// 2번풀이 (hashSet)
function longestConsecutive(nums: number[]): number {
  const numSet = new Set(nums);
  let max = 0;

  for (const num of numSet) {
    // 수열의 시작점인 경우만 탐색
    if (!numSet.has(num - 1)) {
      let current = num;
      let count = 1;

      while (numSet.has(current + 1)) {
        current++;
        count++;
      }

      max = Math.max(max, count);
    }
  }

  return max;
};
