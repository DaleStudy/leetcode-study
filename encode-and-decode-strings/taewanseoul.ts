/**
 * 659 · Encode and Decode Strings
 * Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
 * Please implement encode and decode
 *
 * https://leetcode.com/problems/encode-and-decode-strings/description/
 * https://www.lintcode.com/problem/659/
 *
 */

// O(n) time
// O(1) space
function encode(strs: string[]): string {
  let result = "";

  for (const str of strs) {
    result += `${str.length}#${str}`;
  }

  return result;
}

// O(n) time
// O(n) space
function decode(str: string) {
  const result: string[] = [];

  let i = 0;
  while (i < str.length) {
    let pos = str.indexOf("#", i);
    const len = Number(str.slice(i, pos));
    const word = str.slice(pos + 1, pos + 1 + len);
    result.push(word);
    i = pos + 1 + len;
  }

  return result;
}
