/**
 * 문제 파악: 배열에서 가장 자주 등장하는 k개의 요소를 찾는 문제
 *
 * 접근 방식:
 * (1) Map을 사용하여 각 숫자가 배열에서 몇 번 등장하는지 빈도수 계산
 * (2) 문제의 요구사항에 따라 O(n log n)보다 빠른 시간 복잡도가 필요 => 버킷 정렬 활용 - 시간 복잡도 O(n)
 * (3) 가장 높은 빈도수를 가진 버킷부터 시작하여 k개의 요소를 결과 배열에 추가하여 리턴
 *
 * 코드 설명:
 * 각 숫자의 빈도수를 저장할 Map 생성해서, 모든 숫자의 빈도수 계산해서 저장
 * 빈도수를 기준으로 내림차순 정렬된 buckets 배열 생성 후,
 * 각 숫자를 빈도수[freq]에 해당하는 버킷에 넣기
 * 결과 리턴할 빈 배열 만들어주고,
 * 가장 높은 빈도수부터 시작하여 k개의 요소를 결과 배열에 추가
 * 반복문 끝나면 결과값 리턴
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const frequencyMap = new Map();

  for (const num of nums) {
    frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
  }

  const buckets = Array(nums.length + 1)
    .fill()
    .map(() => []);

  for (const [num, freq] of frequencyMap) {
    buckets[freq].push(num);
  }

  const result = [];

  for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
    if (buckets[i].length > 0) {
      result.push(...buckets[i].slice(0, k - result.length));
    }
  }

  return result;
};
