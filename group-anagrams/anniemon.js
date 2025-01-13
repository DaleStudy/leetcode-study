/**
 * 시간 복잡도:
 *   정렬 작업은 각 문자열의 길이가 m일 때 O(m logm)이고, 총 strs의 길이만큼 수행되므로
 *   시간 복잡도는 O(n * mlogm)
 * 공간 복잡도:
 *   Map 키는 최대 길이 m인 문자열 strs.length개이다.
 *   따라서 공간 복잡도는 O(n * m)
 */
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
  const map = new Map();
  for(const s of strs) {
      const key = s.split('').sort().join('');
      if(!map.has(key)) {
          map.set(key, [])
      }
      map.get(key).push(s);
  }
  return Array.from(map.values());
};
