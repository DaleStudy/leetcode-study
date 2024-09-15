/**
 * https://leetcode.com/problems/group-anagrams/description
 * T.C: O(n * m * log(m)), n = strs.length, m = max(strs[i].length)
 * S.C: O(n * m)
 */
function groupAnagrams(strs: string[]): string[][] {
  const map = new Map<string, string[]>();

  for (const str of strs) { // O(n)
    const sorted = str.split('').sort().join(''); // O(m * log(m))

    if (map.has(sorted))
      map.get(sorted)!.push(str);
    else
      map.set(sorted, [str]);
  }

  return Array.from(map.values());
}
