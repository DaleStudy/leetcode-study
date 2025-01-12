/**
 * https://www.lintcode.com/problem/659/
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

function encode(strs: string[]): string {
  return strs.join("😀");
}

function decode(str: string): string[] {
  return str.split("😀");
}

decode(encode(["Hello", "World"]));
/*
 * output
 * ["Hello","World"]
 */
