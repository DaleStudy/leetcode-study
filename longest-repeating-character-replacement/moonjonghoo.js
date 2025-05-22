/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let left = 0;
  let maxCount = 0;
  let freq = new Array(26).fill(0); // A~Z

  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    const idx = s.charCodeAt(right) - "A".charCodeAt(0);
    freq[idx]++;
    maxCount = Math.max(maxCount, freq[idx]);

    let windowSize = right - left + 1;

    if (windowSize - maxCount > k) {
      const leftIdx = s.charCodeAt(left) - "A".charCodeAt(0);
      freq[leftIdx]--;
      left++;
    }

    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
};
