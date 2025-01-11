// 시간복잡도: O(n * m log m)
// 공간복잡도: O(n)

// HashMap 사용
// 각 문자열을 정렬하여 키로 사용
// 정렬된 문자열을 키로 사용하여 그룹화

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const map = {};

  for (const str of strs) {
    const key = str.split('').sort().join('');
    if (!map[key]) {
      map[key] = [];
    }
    map[key].push(str);
  }

  return Object.values(map);
};
