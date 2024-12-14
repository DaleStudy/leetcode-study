/**
 * Source: https://leetcode.com/problems/top-k-frequent-elements/
 * 풀이방법: 순회를 통해 빈도수를 저장, Object.entries를 통해 정렬하여 k개까지 반환
 * 시간복잡도: O(nlogn)
 * 공간복잡도: O(n)
 *
 * 생각나는 풀이방법
 */
function topKFrequent(nums: number[], k: number): number[] {
  const KFrequentObject = new Object();
  const result = new Array();
  for (let num of nums) {
    if (!Object.hasOwn(KFrequentObject, num)) KFrequentObject[num] = 0;
    KFrequentObject[num]++;
  }
  // Object.entries를 통해 key, value를 배열로 반환 (포인트)
  let sorted = Object.entries(KFrequentObject).sort((a, b) => b[1] - a[1]);
  for (let node of sorted) {
    result.push(parseInt(node[0]));
  }
  return result.slice(0, k);
}
