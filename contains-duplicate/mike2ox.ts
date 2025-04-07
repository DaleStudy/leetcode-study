/**
 * Source: https://leetcode.com/problems/contains-duplicate/
 * 문제 통과 시간: 5분
 * 풀이방법: Set을 이용하여 중복된 값이 있는지 확인
 * 시간복잡도: O(n) - nums를 자료구조 Set에 저장하는 시간
 * 공간복잡도: O(n) - 겹치지 않는 경우 nums만큼의 공간이 필요
 *
 * 생각나는 풀이방법
 * 1. 단순하게 sorted를 이용하여 이전값과 비교하여 중복된 값이 있는지 확인
 * 2. 정렬하지 않고 nums의 길이만큼의 배열을 만들어서 중복된 값이 있는지 저장하면서 확인
 */
function containsDuplicate(nums: number[]): boolean {
  // NOTE: 기존 코드에서 의미있는 것들만 남김
  return new Set<number>(nums).size !== nums.length;
}
