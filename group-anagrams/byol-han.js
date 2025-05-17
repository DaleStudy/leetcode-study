/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const map = new Map();

  for (let str of strs) {
    // 문자열을 정렬해서 key로 사용
    const key = str.split("").sort().join("");

    // key가 이미 있다면 배열에 추가, 없으면 새로 생성
    if (!map.has(key)) {
      map.set(key, []);
    }
    map.get(key).push(str);
  }

  // 값만 모아서 배열로 반환
  return Array.from(map.values());
};
