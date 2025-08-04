function merge(intervals) {
  if (intervals.length === 0) return [];

  // 1) 시작점 기준 정렬
  intervals.sort((a, b) => a[0] - b[0]);

  const merged = [];
  for (const interval of intervals) {
    // 2) 결과 배열의 마지막 구간
    const last = merged[merged.length - 1];

    // 3) 겹치지 않으면 새 구간 추가
    if (!last || interval[0] > last[1]) {
      merged.push(interval);
    } else {
      // 4) 겹치면 병합: 끝점 확장
      last[1] = Math.max(last[1], interval[1]);
    }
  }
  return merged;
}
