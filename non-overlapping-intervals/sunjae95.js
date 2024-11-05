/**
 * @description
 * overlapping이 안되기위한 기준이 필요함을 느낌
 * 처음에는 시작점, 끝점을 기준으로 정렬했지만 16번 테스트에서 실패
 * 정렬기준이 끝점, 시작점 순으로 정렬해야한다고 깨닫게 됨
 *
 * n = length of intervals
 * time complexity: O(n log n)
 * space complexity: O(n)
 */
var eraseOverlapIntervals = function (intervals) {
  intervals.sort((a, b) => {
    if (a[1] !== b[1]) return a[1] - b[1];
    if (a[0] !== b[0]) return b[0] - a[0];
    return 0;
  });

  let answer = 0;
  const current = intervals[0];

  for (let i = 1; i < intervals.length; i++) {
    const [start, end] = intervals[i];

    if (current[1] > start) answer++;
    else {
      current[0] = start;
      current[1] = end;
    }
  }

  return answer;
};
