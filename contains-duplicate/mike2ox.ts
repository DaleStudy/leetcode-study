/**
 * Source: https://leetcode.com/problems/contains-duplicate/
 * 풀이방법: Set을 이용하여 중복된 값이 있는지 확인
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 *
 * 생각나는 풀이방법
 * 1. 단순하게 sorted를 이용하여 이전값과 비교하여 중복된 값이 있는지 확인
 * 2. 정렬하지 않고 nums의 길이만큼의 배열을 만들어서 중복된 값이 있는지 저장하면서 확인
 */
function containsDuplicate(nums: number[]): boolean {
  // 중복된 값이 없는 자료구조 Set 활용
  const set = new Set<number>(nums);
  // Set의 size와 nums의 length를 비교하여 중복된 값이 있는지 확인
  return set.size !== nums.length;
}
