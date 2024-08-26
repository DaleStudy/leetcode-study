/**
 * @description
 * time complexity: O(N)
 * space complexity: O(N)
 *
 * brainstorming:
 * 1. hash table value compare to count
 *
 * strategy:
 * string change to hash table
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  let answer = true;
  const tableS = convertHashTable(s);
  const tableT = convertHashTable(t);

  tableS.forEach((_, key) => {
    if (tableT.get(key) && tableT.get(key) === tableS.get(key)) return;
    answer = false;
  });

  return answer;
};

const convertHashTable = (str) =>
  str.split("").reduce((map, s) => {
    map.set(s, (map.get(s) ?? 0) + 1);
    return map;
  }, new Map());
