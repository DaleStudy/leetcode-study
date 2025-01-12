// Guided approach
// TC : O(n*k), where n is the number of strings, and k is the average length of each string.
// SC : O(n*k)
// overal time complexity improved : from O(n * klogk) to O(n * k)

/**
 * Time Complexity Breakdown:
 *
 * Step                                    | Time Complexity     | Explanation
 * --------------------------------------- | ------------------- | ----------------------------------------
 * Outer loop over strings (`for` loop)    | O(n)                | Iterate over each string in the input array `strs`.
 * Create key (`createKey`)                | O(k) per string     | For each string, count character frequencies, with k being the length of the string.
 * Map operations (`set` and `get`)        | O(1) per string     | Inserting and retrieving values from a Map.
 * Result array                            | O(n * k)            | Storing grouped anagrams in the result array.
 *
 * Overall Time Complexity:                | O(n * k)            | Total time complexity considering all steps.
 *
 * Space Complexity Breakdown:
 *
 * Step                                    | Space Complexity    | Explanation
 * --------------------------------------- | ------------------- | -----------------------------------------
 * Map to store grouped anagrams           | O(n * k)            | Map stores n groups with each group having at most k characters.
 * Auxiliary space for `createKey`         | O(1)                | The frequency array used to count characters (constant size of 26).
 * Space for the result array              | O(n * k)            | Result array storing n groups of up to k elements.
 *
 * Overall Space Complexity:               | O(n * k)            | Total space complexity considering all storage.
 */

/**
 * @param {string[]} strs
 * @return {string[][]}
 */

var groupAnagrams = function (strs) {
  const createKey = (str) => {
    const arr = new Array(26).fill(0);

    for (const ch of str) {
      const idx = ch.charCodeAt() - "a".charCodeAt();
      arr[idx] += 1;
    }

    return arr.join("#");
  };

  let map = new Map();

  for (const str of strs) {
    const key = createKey(str);
    map.set(key, [...(map.get(key) || []), str]);
  }

  return Array.from(map.values(map));
};

// *My own approach

// Time Complexity
// 1. Sorting Each String:
// Sorting a string takes O(k*logk), where k is the length of the string.
// Since we sort each string in the input array of size n, the total cost for sorting is O(n*klogk).

// 2. Hash Map Operations:
// Inserting into the hash map is O(1) on average. Over n strings, the cost remains O(n).

// Overall Time Complexity:
// O(n*klogk), where n is the number of strings and k is the average length of a string.

// /**
//  * @param {string[]} strs
//  * @return {string[][]}
//  */

// var groupAnagrams = function (strs) {
//   // helper function
//   const sorted = (str) => {
//     return str.split("").sort().join("");
//   };

//   let obj = {};

//   for (const str of strs) {
//     const key = sorted(str);
//     obj[key] = [...(obj[key] || []), str];
//   }

//   return Object.values(obj);
// };
