/**
 * 애너그램끼리 묶어서 반환하는 함수
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = function(strs) {
  // 풀이 1
  // 시간복잡도: O(n*s) (n: strs.length, s: str.length)
  // 공간복잡도: O(n)
  function groupManually () {
    const groups = {};

    strs.forEach((str) => {
        const key = [...str].sort().join('');
        if (!groups[key]) groups[key] = [];
        groups[key].push(str);
    });

    return  Object.values(groups);
  }

  // 풀이 2
  // 시간복잡도: O(n*s) (n: strs.length, s: str.length)
  // 공간복잡도: O(n)
  function groupByAnagram() {
    const result = Object.groupBy(strs, (str) => [...str].sort().join(''));
    return  Object.values(result);
  }

  return groupByAnagram();
};

