/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */

const DELIMITER = "#";

var encode = function (strs) {
  let temp = "";
  for (const str of strs) { // encode using the delimiter by attaching the length of the array as well
    temp += `${str.length}${DELIMITER}` + str; 
  }
  return temp;
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
var decode = function (s) { // decode using the length of array that is attached with the delimiter
  let result = [];
  let i = 0;
  while (i < s.length) {
    let j = i;
    while (s[j] !== DELIMITER) j++;
    const len = Number(s.slice(i, j));
    const word = s.slice(j + 1, j + len + 1);
    result.push(word);
    i = j + len + 1;
  }
  return result;
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */

// test cases
console.log(["Hello", "World"]);

// time - O(n) - iterate through the list of strings once
// space - O(n) - stores the strings
