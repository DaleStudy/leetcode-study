// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function (intervals, newInterval) {
  // 1. Insert newInterval
  const candidates = [];
  let inserted = false;

  if (intervals.length === 0) {
    candidates.push(newInterval);
  }

  for (const [start, end] of intervals) {
    const [newStart, newEnd] = newInterval;

    if (!inserted) {
      if (newStart <= start) {
        candidates.push([newStart, newEnd]);
        inserted = true;
      }
    }

    candidates.push([start, end]);
  }

  if (!inserted) {
    candidates.push(newInterval);
  }

  // 2. Merge if needed

  const answer = [];

  for (const [start, end] of candidates) {
    if (answer.length === 0) {
      answer.push([start, end]);
      continue;
    }

    const [compareStart, compareEnd] = answer.at(-1);

    if (compareEnd >= start) {
      answer.pop();
      answer.push([Math.min(start, compareStart), Math.max(end, compareEnd)]);
      continue;
    }

    answer.push([start, end]);
  }

  return answer;
};
