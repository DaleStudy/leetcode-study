function insert(intervals: number[][], newInterval: number[]): number[][] {
  const result: number[][] = [];
  let i = 0;

  while (i < intervals.length && newInterval[0] > intervals[i][1]) {
    result.push(intervals[i]);
    i++;
  }

  while (i < intervals.length && newInterval[1] >= intervals[i][0]) {
    newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
    newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
    i++;
  }
  result.push(newInterval);

  while (i < intervals.length) {
    result.push(intervals[i]);
    i++;
  }

  return result;
}
