/**
 * 문자열 배열 strs가 주어졌을 때, 애너그램끼리 그룹화하는 문제
 * 애너그램: 같은 문자를 재배열하여 만들 수 있는 단어들
 *
 * 접근 방법: 각 문자 출현빈도를 카운팅하는 방식
 * 1. 각 문자열을 알파벳 개수로 변환하여 키를 생성
 * 2. Map을 사용하여 키를 기준으로 문자열을 그룹화
 * 3. Map의 값들을 배열로 변환하여 반환
 *
 * 시간복잡도: O(n * k) (n: 문자열 개수, k: 문자열 길이) -> 단순 카운팅
 * 공간복잡도: O(n * k) -> 모든 문자열을 저장해야 하므로
 */

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const map = new Map();

  for (let str of strs) {
    const count = new Array(26).fill(0); // 알파벳 개수 초기화
    for (let i = 0; i < str.length; i++) {
      const index = str.charCodeAt(i) - 'a'.charCodeAt(0); // 알파벳 인덱스 계산
      count[index]++; // 해당 알파벳 개수 증가
    }
    const key = count.join('#'); // 알파벳 개수를 문자열로 변환하여 키 생성
    if (!map.has(key)) {
      map.set(key, []); // 키가 없으면 새로운 배열 생성
    }
    map.get(key).push(str); // 해당 키에 문자열 추가
  }

  return Array.from(map.values()); // Map의 값들을 배열로 변환하여 반환
};
