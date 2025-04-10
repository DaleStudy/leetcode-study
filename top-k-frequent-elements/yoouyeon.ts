/**
 * [Idea]
 * 숫자와 등장 횟수를 세는 counter Map을 활용했다.
 * 1. counter Map을 만든 뒤
 * 2. 배열로 변환
 * 3. count 내림차순으로 정렬
 * 4. 정답 배열 만들기
 *
 * [Time Complexity]
 * O(n + m log m) => O(n log n) (n: nums의 길이, m: nums에서 unique elements의 개수)
 * - counter Map을 생성할 때 O(n)
 * - counter를 배열로 변환해서 정렬할 때 O(m log m)
 * - sortedCounter를 k 길이로 자르고 count만 담은 배열로 만들 때 O(k)
 *
 * [Space Complexity]
 * O(m + k) => O(n)
 * - counter Map의 O(m)
 * - 정답 배열을 만들 때 추가로 사용하는 O(k)
 */
function topKFrequent1(nums: number[], k: number): number[] {
  const counter = new Map<number, number>(); // key: 숫자, value: count
  for (const num of nums) {
    const count = counter.get(num);
    counter.set(num, count === undefined ? 1 : count + 1);
  }

  const sortedCounter = [...counter].sort((a, b) => b[1] - a[1]);
  return sortedCounter.slice(0, k).map((count) => count[0]);
}
