/*
  시간복잡도: O(n) - 모든 요소에 대해 최대 한 번씩만 검사하기 때문
  - Set을 사용하여 O(1) 시간에 요소 존재 여부 확인 가능
  - 각 숫자는 연속 수열의 시작점인 경우에만 while 루프를 실행
    -> 모든 요소에 대해 while 루프의 총 반복 횟수는 전체 요소 수를 초과하지 않음
*/
/**
 * @param {number[]} nums
 * @return {number}
 */

var longestConsecutive = function (nums) {
  const numSet = new Set(nums);
  let longest = 0;

  for (let n of [...numSet]) {
    if (!numSet.has(n - 1)) {
      let length = 0;
      while (numSet.has(n + length)) {
        length += 1;
      }
      longest = Math.max(length, longest);
    }
  }
  return longest;
};
