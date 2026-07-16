/**
 * 풀이
 * 1. 두 문자열의 길이가 다르면 false를 반환한다.
 * 2. 첫 번째 문자열을 순회하며 각 문자의 등장 횟수를 count 객체에 저장한다.
 * 3. 두 번째 문자열을 순회하며 count 객체에서 해당 문자의 등장 횟수를 감소시킨다.
 * 4. 만약 count 객체에 해당 문자가 없거나 등장 횟수가 0이면 false를 반환한다.
 * 5. 모든 문자를 순회한 후에도 false를 반환하지 않았다면 true를 반환한다.
 * 시간 복잡도 - O(n) : 두 문자열을 한 번씩 순회
 * 공간 복잡도 - O(1) : count 객체는 최대 26개의 알파벳만 저장
 */
var isAnagram = function (s, t) {
  let count = {};
  if (s.length !== t.length) {
    return false;
  }
  for (const i of s) {
    count[i] = count[i] ? count[i] + 1 : 1;
  }
  for (const i of t) {
    if (!count[i]) return false;
    count[i]--;
  }
  return true;
};
