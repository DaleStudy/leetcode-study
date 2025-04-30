// Approach 2
// Time Complexity: O(n * L), where n = number of strings in strs, L = maximum length of a string in strs
// Space Complexity: O(n * L)

function groupAnagrams(strs: string[]): string[][] {

  let sorted: { [key: string]: string[] } = {}

  for (const str of strs) {

      const arr = Array.from({ length: 26 }, () => 0)

      for (const ch of str) {
          arr[ch.charCodeAt(0) - "a".charCodeAt(0)] += 1
      }

      // const key = arr.join(""); // This can lead to key collisions.
      const key = arr.join("#"); // ✅

      if (!sorted[key]) {
          sorted[key] = []
      }

      sorted[key].push(str)
  }

  return Object.values(sorted);
};


// Approach 1
// Time Complexity: O(n * LlogL), where n = number of strings, L = average length of the strings
// Space Complexity: O(n * L)

// function groupAnagrams(strs: string[]): string[][] {
//   // input: an array of strings, strs
//   // output: the anagrams

//   // eat -> e, a, t -> a, e, t
//   // tea -> t, e, a -> a, e, t
//   // ate -> a, t, e -> a, e, t

//   let map = new Map<string, string[]>();
//   let result: string[][] = [];

//   for (const str of strs) {
//     const temp = str.split("").sort().join("");

//     if (map.has(temp)) {
//       map.set(temp, [...map.get(temp)!, str]);
//     } else {
//       map.set(temp, [str]);
//     }
//   }

//   for (const el of map.values()) {
//     result.push(el);
//   }

//   return result;
// }

