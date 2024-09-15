/**
 * TC: O(N * S)
 * SC: O(N)
 * N: strs.length, S: Max(strs[i].length)
 *
 * 풀이
 * 주어진 배열 strs의 각 원소의 키를 구해서 같은 원소끼리 묶어 정답을 찾는다.
 * 키 구하는 방법은 주어진 문자열의 사용된 알파벳 갯수이다.
 */

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  // 1. 키를 저장할 Map
  const keyMap = new Map();

  for (const str of strs) {
    // 2. 키를 구해서 동일한 키면 같은 값(배열)에 추가한다.
    const key = generateKey(str);

    if (keyMap.has(key)) {
      keyMap.get(key).push(str);
    } else {
      keyMap.set(key, [str]);
    }
  }

  // 3. 키를 저장한 Map의 값들을 모아 정답을 반환한다.
  const result = [];

  for (const v of keyMap.values()) {
    result.push(v);
  }

  return result;

  // 키 구하는 함수
  function generateKey(str) {
    // 각 알파벳이 몇개 등장했는지 기록할 배열
    const usedCount = new Array(26).fill(0);

    for (const s of str) {
      // 아스키코드로 변환하여 index를 구한다.
      usedCount[s.charCodeAt() - 97] += 1;
    }

    return usedCount.join(",");
  }
};
