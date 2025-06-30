// TC: O(n log n)
// SC: O(1)
function eraseOverlapIntervals(intervals: number[][]): number {
  intervals.sort((a, b) => a[1] - b[1]);
  // [1, 2], [2, 3], [1, 3], [3, 4]

  let prevEnd = intervals[0][1];
  let removalCount = 0;

  for (let i = 1; i < intervals.length; i++) {
    if (prevEnd > intervals[i][0]) {
      removalCount++;
      // skip current interval
    } else {
      prevEnd = intervals[i][1];
    }
  }

  return removalCount;
}


// TC: O(n log n)
// SC: O(1)
// function eraseOverlapIntervals(intervals: number[][]): number {
//   intervals.sort((a, b) => a[0] - b[0]);

//   let prev = intervals[0];
//   let cnt = 1;
//   let removalCount = 0;

//   while (cnt < intervals.length) {
//     const current = intervals[cnt];

//     if (prev[1] <= current[0]) {
//       prev = current;
//     } else {
//       prev = [Math.min(prev[0], current[0]), Math.min(prev[1], current[1])];
//       removalCount++;
//     }
//     cnt++;
//   }

//   return removalCount;
// }

