var characterReplacement = function (s, k) {
  // Create two pointer to check repeating chracter (left, right)
  let left = 0,
    right = 0,
    maxCount = 0,
    map = new Map();

  while (right < s.length) {
    // Save each character into map and check how many time they have
    map.set(s[right], map.get(s[right]) ? map.get(s[right]) + 1 : 1);
    maxCount = Math.max(maxCount, map.get(s[right]));

    // Count (right-left+1-k) and compare maximum value
    if (right - left + 1 - k > maxCount) {
      // Decrement value of map[s[left]] and move left pointer
      map.set(s[left], map.get(s[left]) - 1);
      left++;
    }

    right++;
  }

  return right - left;
};

// TC: O(n)
// SC: O(1)
