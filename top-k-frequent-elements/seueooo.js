/**
 * 풀이
 * 해시맵을 사용하여 각 숫자의 빈도를 저장하고, 그 값을 기준으로 정렬하여 상위 k개의 요소를 선택한다.
 * 시간 복잡도 - O(n log n) : 해시맵 생성 O(n) + 정렬 O(n log n)
 * 공간 복잡도 - O(n) : 해시맵 저장 공간
 */
var topKFrequent = function (nums, k) {
  let map = {};
  for (const n of nums) {
    map[n] = map[n] ? map[n] + 1 : 1;
  }
  const sorted = Object.entries(map).sort((a, b) => b[1] - a[1]);
  let answer = [];
  for (let i = 0; i < k; i++) {
    answer.push(Number(sorted[i][0]));
  }
  return answer;
};
