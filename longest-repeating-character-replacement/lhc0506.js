/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
  let start = 0;
  let maxFreq = 0;
  let result = 0;
  const map = new Map();

  for (let end = 0; end < s.length; end++) {
      const endChar = s[end];
      map.set(endChar, 1 + (map.get(endChar) || 0));

      maxFreq = Math.max(maxFreq, map.get(endChar));

      if (end - start + 1 - maxFreq > k) {
          const startChar = s[start];
          map.set(startChar, map.get(startChar) - 1);
          start++;

      }

      result = Math.max(result, end - start + 1);
  }

  return result;
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
