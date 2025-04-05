/**
 * Source: https://leetcode.com/problems/top-k-frequent-elements/
 * 요점: 배열에서 가장 빈번하게 등장하는 k개의 요소를 반환
 * 풀이 시간: 27분
 * 풀이방법: 순회를 통해 빈도수를 저장, Object.entries를 통해 정렬하여 k개까지 반환
 * 시간복잡도: O(nlogn) - n은 nums의 크기, 정렬 연산이 지배적
 * 공간복잡도: O(n) - 최악의 경우 모든 요소가 고유할 때
 */
function topKFrequent(nums: number[], k: number): number[] {
  // 각 숫자의 빈도수를 기록하는 Map
  const frequencyMap = new Map<number, number>();

  // 모든 숫자의 빈도수 계산
  for (const num of nums) {
    frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
  }

  // 빈도수에 따라 내림차순으로 정렬
  const sortedEntries = Array.from(frequencyMap.entries()).sort(
    (a, b) => b[1] - a[1]
  );

  // 상위 k개 요소 추출
  return sortedEntries.slice(0, k).map((entry) => entry[0]);
}
