// Time complexity: O(n^2)
// Space complexity: O(n)

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  intervals.sort((a, b) => {
    if (a[0] === b[0]) {
      return a[1] - b[1];
    }

    return a[0] - b[0];
  });

  const dp = Array.from({ length: intervals.length }, () => 0);

  dp[0] = 1;

  for (let i = 1; i < intervals.length; i++) {
    const [prevStart, prevEnd] = intervals[i - 1];
    const [currentStart, currentEnd] = intervals[i];

    // 구간이 겹칠 때
    if (currentStart < prevEnd) {
      // 현재를 포함할 때
      let maxValue = 1;
      for (let j = i - 1; j >= 0; j--) {
        const [start, end] = intervals[j];

        if (end <= currentStart) {
          maxValue += dp[j];
          break;
        }
      }

      dp[i] = Math.max(dp[i - 1], maxValue);
      continue;
    }

    // 구간이 겹치지 않을 때
    dp[i] = dp[i - 1] + 1;
  }

  return intervals.length - dp.at(-1);
};
