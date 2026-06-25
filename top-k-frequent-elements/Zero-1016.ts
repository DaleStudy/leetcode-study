/**
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 * 배열에서 각 숫자의 빈도를 계산한 후 상위 k개의 빈도 요소를 반환한다.
 */
function topKFrequent(nums: number[], k: number): number[] {
  const count = new Map<number, number>();

  for (const number of nums) {
    count.set(number, (count.get(number) ?? 0) + 1);
  }
  // [1, 1, 3, 2, 2, 2, 3, 3, 3]이 들어오면
  // Map { 1 => 2, 3 => 4, 2 => 3 } 이 됩니다.

  const answer = [...count.keys()];
  answer.sort((a, b) => count.get(b)! - count.get(a)!);

  return answer.slice(0, k);
}
