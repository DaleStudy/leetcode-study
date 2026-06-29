/**
reduce()를 사용하여 배열에서 각 원소의 빈도수를 구한다.
"버킷 정렬"을 사용한 풀이: 원본 배열의 N+1개의 빈 배열을 생성해서 오름차순으로 원소의 빈도수를 넣는다.
- 장점: 시간복잡도가 빠름 O(N)
- 단점: 케이스에 따라 빈 메모리가 많이 소모됨
버킷에서 뒤 원소(빈도수가 많은)부터 하나씩 배열에 넣는다.

문제: Example 3 빈도수가 동일한 경우는 bucket의 원소가 "[1, 2]"로 출력됨.
원인: 이를 1개의 원소로 보았고, length === k 조건에 맞지 않음 → undefined
+ 기존 bucket[i] > 0의 비교는 number일때만 가능하기 때문에 push도 되지않음.

해결: bucket[i].length > 0 길이로 비교, slice + map처리로 [1, 2] 예외 케이스 해결
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
function topKFrequent(nums, k) {
  let result = [];

  let frequency = nums.reduce((acc, count) => {
    acc[count] = (acc[count] || 0) + 1;
    return acc;
  }, {});

  let bucket = Array.from({ length: nums.length + 1 }, () => []);

  for (const [num, count] of Object.entries(frequency)) {
    bucket[count].push(Number(num));
  }

  for (let i = bucket.length - 1; i >= 0; i--) {
    if (bucket[i].length > 0) {
      result.push(...bucket[i]);
    }
  }
  return result.slice(0, k);
}
