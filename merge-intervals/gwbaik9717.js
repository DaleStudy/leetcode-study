// Time complexity: O(nlogn)
// Space complexity: O(n)

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  intervals.sort((a, b) => {
    if (a[0] === b[0]) {
      return a[1] - b[1];
    }

    return a[0] - b[0];
  });

  const answer = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const current = intervals.at(i);
    const prev = answer.at(-1);

    // No overlapping
    if (current[0] > prev[1]) {
      answer.push(current);
      continue;
    }

    answer[answer.length - 1] = [prev[0], Math.max(prev[1], current[1])];
  }

  return answer;
};
