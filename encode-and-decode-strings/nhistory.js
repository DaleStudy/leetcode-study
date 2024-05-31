class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    let result = "";
    for (let str of strs) {
      result += str.length.toString() + "#" + str;
    }
    return result;
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    let result = [];
    let i = 0;

    while (i < str.length) {
      // Find the position of the next '#'
      let j = i;
      while (str[j] !== "#") {
        j++;
      }

      // Length of the next string
      const len = parseInt(str.slice(i, j));
      i = j + 1; // Move past the '#'

      // Extract the string of length 'len'
      result.push(str.slice(i, i + len));
      i += len; // Move past the extracted string
    }

    return result;
  }
}

// TC: O(n),O(n)
// SC: O(n),O(n)
