function eraseOverlapIntervals(intervals: number[][]): number {
  intervals.sort((a, b) => a[1] - b[1]);

  let removedCount = 0;
  let prevEnd = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    const [start, end] = intervals[i];

    if (prevEnd > start) {
      removedCount++;
    } else {
      prevEnd = end;
    }
  }

  return removedCount;
}
