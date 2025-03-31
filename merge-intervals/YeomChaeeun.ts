/**
 * 겹치는 구간 합치기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n log n) - sort() 영향
 * - 공간 복잡도: O(n)
 * @param intervals
 */
function merge(intervals: number[][]): number[][] {
  if(intervals.length === 1) return intervals

  intervals.sort((a, b) => a[0] - b[0]);

  let results: number[][] = []
  let [tempX, tempY] = intervals[0]

  for(let i = 1; i < intervals.length; i++) {
    let [x, y] = intervals[i]
    if(x <= tempY) {
      tempY = Math.max(tempY, y)
    } else {
      results.push([tempX, tempY])
      tempX = x
      tempY = y
    }
  }
  results.push([tempX, tempY])

  return results;
}
