var lengthOfLongestSubstring = function (s) {
  // Create map to store character from string
  let map = new Map();
  let maxLen = 0;
  let start = 0;

  for (let end = 0; end < s.length; end++) {
    if (map.has(s[end])) {
      // Move the start pointer to the right of the previous position of current character
      start = Math.max(map.get(s[end]) + 1, start);
    }
    map.set(s[end], end);
    maxLen = Math.max(maxLen, end - start + 1);
  }
  return maxLen;
};

// TC: O(n)
// SC: O(n)
