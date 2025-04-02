/**
 * 시간 복잡도: O(n log n)
 * - nums 배열 순회하며 빈도수 카운트: O(n)
 * - 빈도수 기준 내림차순 정렬: O(n log n)
 * - 상위 k개 선택: O(k) -> k는 n보다 작으므로 무시
 *
 * 공간 복잡도: O(n)
 * - countNums 객체: 최악의 경우 모든 숫자가 다른 경우 O(n)
 * - sortedCountNums 배열: countNums와 동일한 크기 O(n)
 * - answer 배열: k 크기이지만 k는 n보다 작으므로 무시
 */
const topKFrequent = (nums, k) => {
  // 각 숫자의 빈도수를 저장하는 객체
  const countNums = {};

  // nums 배열을 순회하며 각 숫자의 빈도수를 카운트
  for (let i = 0; i < nums.length; i += 1) {
    const num = nums[i];
    countNums[num] = !countNums[num] ? 1 : countNums[num] + 1;
  }

  // 빈도수를 기준으로 내림차순 정렬
  const sortedCountNums = Object.entries(countNums).sort((a, b) => b[1] - a[1]);
  const answer = [];

  // 상위 k개의 숫자를 answer 배열에 저장
  for (let i = 0; i < k; i += 1) {
    answer[i] = Number(sortedCountNums[i][0]);
  }

  return answer;
};
