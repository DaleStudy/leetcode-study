/**
 * @description
 * brainstorming:
 * two pointer + hash table
 *
 * n = length of s
 * m = length of t
 * time complexity: O(n*n)
 * space complexity: O(n)
 */
var minWindow = function (s, t) {
  const requiredMap = t.split("").reduce((map, char) => {
    map.set(char, (map.get(char) ?? 0) + 1);
    return map;
  }, new Map());
  const requiredArray = [...requiredMap.entries()];
  const map = new Map();
  const successRequired = () =>
    requiredArray.every(([key, value]) => map.get(key) >= value);

  let answer = "";
  let start = 0;

  for (let i = 0; i < s.length; i++) {
    if (requiredMap.has(s[i])) map.set(s[i], (map.get(s[i]) ?? 0) + 1);

    while (successRequired()) {
      const now = s.slice(start, i + 1);
      answer = answer === "" || answer.length >= now.length ? now : answer;

      if (map.has(s[start])) {
        map.set(s[start], map.get(s[start]) - 1);
        if (map.get(s[start]) === -1) map.delete(s[start]);
      }

      start++;
    }
  }

  return answer;
};
