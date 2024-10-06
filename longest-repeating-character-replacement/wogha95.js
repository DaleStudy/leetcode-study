/**
 * 알고달레 풀이 참고
 * @see https://www.algodale.com/problems/longest-repeating-character-replacement/
 *
 * TC: O(S)
 * right의 순회 + left의 순회
 * (곱이 아닌 더하기인 이유는 right 순회동안 left 순회의 최대 총합이 S이기 때문입니다.)
 *
 * SC: O(1)
 * 최악의 경우 26개의 소문자를 저장하는 memoryMap으로 인해 상수 복잡도를 갖게 됩니다.
 *
 * S: s.length
 */

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  // 1. 가장 긴 subString 길이
  let result = 0;

  // 2. left, right 포인터 사이에서 등장한 문자 횟수를 기록한 Map과 최다 등장한 횟수를 기록한 변수
  const memory = new Map();
  let maxCount = 0;

  let left = 0;
  let right = 0;

  while (right < s.length) {
    // 3. '새로운 문자(s[right])의 갯수 기록'과 '최다 등장한 횟수 갱신'
    const newCount = (memory.has(s[right]) ? memory.get(s[right]) : 0) + 1;
    memory.set(s[right], newCount);
    maxCount = Math.max(maxCount, newCount);

    // 4. k만큼 변경가능한 subString 길이를 맞추기 위해 left 이동
    while (right - left + 1 - maxCount > k) {
      const newCount = memory.get(s[left]) - 1;
      memory.set(s[left], newCount);
      left += 1;
    }

    // 5. 가장 긴 subString 길이 갱신, right 이동
    result = Math.max(result, right - left + 1);
    right += 1;
  }

  return result;
};
