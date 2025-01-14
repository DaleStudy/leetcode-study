/**
 * @param {string[]} strs
 * @return {string[][]}
 * 
 * complexity
 * time: O(n * m)
 * space: O(n)
 * 
 * 풀이
 * 처음에는 각 알파벳에 숫자를 할당하여 합을 이용해서 풀이하는 방식으로 접근하려고 했으나,
 * 합의 경우의 수가 너무 많아서 중복되는 경우가 생겨서 다른 풀이 방식을 생각했다.
 * -> 이후 소수를 이용한 풀이를 생각했다. (소수의 곱을 이용하는 경우 중복되는 경우가 없다.)
 *    하지만 최악의 경우 소수의 곱이 너무 커져서 오버플로우가 발생한다.
 * 
 * 그래서 정렬을 통해 각 문자열을 정렬하여 키로 사용하는 방식으로 접근했다.
 */
var groupAnagrams = function(strs) {
  const map = new Map();
  
  for(const str of strs) {
      const sortedStr = str.split('').sort().join('');
      
      if(!map.has(sortedStr)) {
          map.set(sortedStr, []);
      }
      map.get(sortedStr).push(str);
  }
  
  return Array.from(map.values());
};

/**
 * passed 되었으나, 최악의 경우에는 통과될 수 없지 않을까?
 * 
 * @param {string[]} strs
 * @return {string[][]}
 * 
 * complexity
 * time: O(n * m)
 * space: O(n)
 */
var groupAnagrams = function(strs) {
  const map = new Map();
  
  const primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,
                 43,47,53,59,61,67,71,73,79,83,89,97,101];
  
  for(const str of strs) {
      let key = 1;
      for(const char of str) {
          key *= primes[char.charCodeAt(0) - 'a'.charCodeAt(0)];
      }
      
      if(!map.has(key)) {
          map.set(key, []);
      }
      map.get(key).push(str);
  }
  
  return Array.from(map.values());
};

