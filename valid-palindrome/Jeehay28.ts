// Approach 2
// 🗓️ 2025-04-14
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(1)

function isPalindrome(s: string): boolean {
  let low = 0, high = s.length - 1;
  const reg = /[0-9a-zA-Z]/;

  while (low < high) {
    while (low < high && !reg.test(s[low])) {
      low += 1;
    }

    while (low < high && !reg.test(s[high])) {
      high -= 1;
    }

    if (s[low].toLowerCase() !== s[high].toLowerCase()) {
      return false;
    }
    low += 1;
    high -= 1;
  }

  return true;
}


// Approach 1
// 🗓️ 2025-04-14
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(n)

// function isPalindrome(s: string): boolean {
//   // cover all uppercase letters into lowercasse letters
//   // remove all non-alphanumeric characters (letters and numbers)
//   // it reads the same forward and backward

//   const cleaned = s.toLowerCase().match(/[0-9a-z]/g);

//   // Converting to lowercase (toLowerCase()): O(n), where n is the length of the string
//   // Matching with regex (match(/[0-9a-z]/g)): O(n), where n is the length of the string, as the regex engine needs to check each character in the string
//   // join("") operation: O(m), where m is the length of the cleaned array.
//   // reverse() operation: O(m), where m is the length of the cleaned array.
//   // Comparison (s_forward === s_backward): O(n) because it checks each character one by one

//   if (cleaned !== null) {
//     const s_forward = cleaned.join("");
//     const s_backward = cleaned.reverse().join("");
//     return s_forward === s_backward;
//   } else {
//     return true;
//   }
// }
