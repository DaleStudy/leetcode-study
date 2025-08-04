// https://neetcode.io/problems/string-encode-and-decode

class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    let encodedStrings: string[] = [];

    for (const word of strs) {
      const length = word.length;
      encodedStrings.push(`${length}#${word}`);
    }

    return encodedStrings.join("");
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    const decodedStrings: string[] = [];
    let position = 0;

    while (position < str.length) {
      const hashIndex = str.indexOf("#", position);
      const length = Number(str.slice(position, hashIndex));

      const start = hashIndex + 1;
      const end = start + length;
      const word = str.slice(start, end);
      decodedStrings.push(word);

      position = end;
    }

    return decodedStrings;
  }
};
