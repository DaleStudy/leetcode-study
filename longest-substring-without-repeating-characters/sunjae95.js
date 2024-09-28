/**
 * @description
 * brainstorming:
 * hash table + two pointer
 *
 * n = length of s
 * time complexity: O(n)
 * space complexity: O(n)
 */
var lengthOfLongestSubstring = function (s) {
  const map = new Map();
  let answer = 0;
  let start = 0;

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) start = Math.max(map.get(s[i]) + 1, start);
    map.set(s[i], i);
    answer = Math.max(answer, i - start + 1);
  }

  return answer;
};
