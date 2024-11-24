/**
 * @param {string} str
 * @param {number} maxConvertCount
 * @return {number}
 */
var characterReplacement = function (str, maxConvertCount) {
  const freqInWindow = {};
  let maxLength = 0;
  let maxCharFreqInWindow = 0;
  let leftIndex = 0;

  for (let rightIndex = 0; rightIndex < str.length; rightIndex++) {
    const slidingWindow = [str[leftIndex], str[rightIndex]];
    const [leftChar, rightChar] = slidingWindow;

    freqInWindow[rightChar] = (freqInWindow[rightChar] || 0) + 1;
    maxCharFreqInWindow = Math.max(
      maxCharFreqInWindow,
      freqInWindow[rightChar]
    );

    // while (currentWindowLength > maxConvertCount + maxCharFreqInWindow) {
    // while (cannot convert all characters in the window to the same character) {
    while (rightIndex - leftIndex + 1 > maxConvertCount + maxCharFreqInWindow) {
      leftIndex += 1;
      freqInWindow[leftChar] -= 1;
    }

    maxLength = Math.max(maxLength, rightIndex - leftIndex + 1);
  }

  return maxLength;
};

/**
 * Time Complexity: O(n)
 * - The right pointer iterates through the string once, making it O(n).
 * - The left pointer only moves when necessary, also contributing to O(n) overall.
 * - Thus, the total time complexity is O(n).
 *
 * Space Complexity: O(1)
 * - The frequency object stores counts for at most 26 letters in the English alphabet.
 * - Since the space used by the frequency object is constant and does not scale with input size,
 *   the space complexity is O(1).
 */
