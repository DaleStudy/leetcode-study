/**
 * @description
 * 각 intervals의 시작점을 기준으로 정렬 후 tmp의 end와 각 start를 비교하여 풀이
 *
 * n = length of intervals
 * time complexity: O(n log n)
 * space complexity: O(n)
 */
var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);

  const answer = [];
  let mergeTmp = intervals[0];

  for (let i = 1; i < intervals.length; i++) {
    const [start, end] = intervals[i];

    if (mergeTmp[1] >= start) mergeTmp[1] = Math.max(mergeTmp[1], end);
    else {
      answer.push(mergeTmp);
      mergeTmp = [start, end];
    }
  }

  answer.push(mergeTmp);

  return answer;
};
