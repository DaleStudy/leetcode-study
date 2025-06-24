function insert(intervals: number[][], newInterval: number[]): number[][] {
  const res: number[][] = [];
  let i = 0;
  const n = intervals.length;

  // 1. newInterval보다 왼쪽에 있는 interval은 그대로 추가
  while (i < n && intervals[i][1] < newInterval[0]) {
    res.push(intervals[i]);
    i++;
  }
  // 2. 겹치는 구간 병합
  while (i < n && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
    newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
    i++;
  }
  res.push(newInterval);

  // 3. 나머지 오른쪽 구간 추가
  while (i < n) {
    res.push(intervals[i]);
    i++;
  }
  return res;
}
