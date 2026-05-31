// 시간 복잡도: O(n) - 각 문자열을 한 번씩만 순회
// 공간 복잡도: O(1) - 최대 26개의 소문자만 저장 (상수 공간)

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = (s, t) => {
  // 길이 체크는 필수
  if (s.length !== t.length) {
    return false;
  }

  // 각 문자의 개수를 저장할 객체
  const charCount = {};

  // 첫 번째 문자열의 각 문자 개수 카운트
  for (let char of s) {
    charCount[char] = (charCount[char] || 0) + 1;
  }

  // 두 번째 문자열의 문자를 하나씩 빼면서 확인
  for (let char of t) {
    if (!charCount[char]) {
      // 없는 문자거나 이미 다 사용한 경우
      return false;
    }
    charCount[char]--;
  }

  return true;
};
