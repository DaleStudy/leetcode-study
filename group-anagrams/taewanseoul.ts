/**
 * 49. Group Anagrams
 * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 *
 * https://leetcode.com/problems/group-anagrams/description/
 */

// O(n * mlog(m)) time
// O(n) space
function groupAnagrams(strs: string[]): string[][] {
  const result: string[][] = [];
  const map = new Map<string, string[]>();

  for (let i = 0; i < strs.length; i++) {
    const word = strs[i];
    const sorted = word.split("").sort().join("");

    if (map.has(sorted)) {
      map.get(sorted)!.push(word);
    } else {
      map.set(sorted, [word]);
    }
  }

  map.forEach((v) => result.push(v));

  return result;
}
