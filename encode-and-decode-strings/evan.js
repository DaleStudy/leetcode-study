const DELIMITER = "#";

/**
 *
 * @param {string[]} strs
 * @returns {string}
 */
function encode(strs) {
  return strs.map((s) => `${s.length}${DELIMITER}${s}`).join("");
}

/**
 *
 * @param {string} encodedStr
 * @returns {string[]}
 */
function decode(encodedStr) {
  const decodedStrings = [];
  let currentIndex = 0;

  while (currentIndex < encodedStr.length) {
    let delimiterIndex = currentIndex;

    while (encodedStr[delimiterIndex] !== DELIMITER) {
      delimiterIndex += 1;
    }

    const strLength = parseInt(
      encodedStr.substring(currentIndex, delimiterIndex)
    );

    decodedStrings.push(
      encodedStr.substring(delimiterIndex + 1, delimiterIndex + 1 + strLength)
    );

    currentIndex = delimiterIndex + 1 + strLength;
  }

  return decodedStrings;
}
/**
 * Time Complexity: O(n) where n is the length of the encoded string.
 * Reason:
 *  The inner operations (finding # and extracting substrings) are proportional to the size of the encoded segments
 *  but are ultimately bounded by the total length of the input string.
 *
 * Space Complexity: O(k) where k is the total length of the decoded strings.
 */

/**
 * Test cases
 */
const strs4 = ["longestword", "short", "mid", "tiny"];
const encoded4 = encode(strs4);
console.log(encoded4); // Output: "11#longestword5#short3#mid4#tiny"

const decoded4 = decode(encoded4);
console.log(decoded4); // Output: ["longestword", "short", "mid", "tiny"]
