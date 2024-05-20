/**
 * @param {string[]} strList
 * @return {string[][]}
 */
var groupAnagrams = function (strList) {
  const map = new Map();

  for (const str of strList) {
    const sortedStr = str.split("").sort().join("");

    if (!map.has(sortedStr)) {
      map.set(sortedStr, []);
    }

    map.get(sortedStr).push(str);
  }

  return Array.from(map.values());
};

/**
 * Time Complexity: O(n * k log k)
 * Reason:
 * - n is the number of strings in the input array.
 * - k is the maximum length of a string in the input array.
 * - Sorting each string takes O(k log k) time.
 * - Thus, sorting all n strings takes O(n * k log k) time.
 *
 * Space Complexity: O(n * k)
 * Reason:
 * - We use a map to store the grouped anagrams.
 * - In the worst case, we might store all n strings in the map.
 * - Each string has a maximum length of k.
 * - Thus, the space complexity is O(n * k).
 */
