// Time Complexity: O(n log n)
// Space Complexity: O(n)
function merge(intervals: number[][]): number[][] {
  const merged: number[][] = [];

  intervals.sort((a, b) => a[0] - b[0]);

  for (const [currentStart, currentEnd] of intervals) {
    if (merged.length === 0 || merged[merged.length - 1][1] < currentStart) {
      merged.push([currentStart, currentEnd]);
    } else {
      const lastMerged = merged[merged.length - 1];
      lastMerged[1] = Math.max(lastMerged[1], currentEnd);
    }
  }

  return merged;
}
