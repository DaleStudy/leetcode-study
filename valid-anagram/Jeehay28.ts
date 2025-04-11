// Approach 2
// 🗓️ 2025-04-06
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(n)

function isAnagram(s: string, t: string): boolean {
  const map = new Map<string, number>();

  for (const char of s) {
    map.set(char, (map.get(char) || 0) + 1);
  }

  for (const char of t) {
    if (!map.has(char)) return false;
    map.set(char, map.get(char)! - 1);
    if (map.get(char) === 0) {
      map.delete(char);
    }
  }

  return map.size === 0;
}


// Approach 1
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(n)

// function isAnagram(s: string, t: string): boolean {
//   const s_map = new Map<string, number>();
//   const t_map = new Map<string, number>();

//   for (const char of s) {
//     s_map.set(char, (s_map.get(char) || 0) + 1);
//   }

//   for (const char of t) {
//     t_map.set(char, (t_map.get(char) || 0) + 1);
//   }

//   // Compare the keys and values of both maps
//   if ([...s_map.keys()].length !== [...t_map.keys()].length) {
//     return false;
//   } else {
//     for (const char of [...s_map.keys()]) {
//       if (s_map.get(char) !== t_map.get(char)) {
//         // Lookup operations in Map are O(1)
//         return false;
//       }
//     }
//   }

//   return true;
// }

