// TC: O(n^2)
// SC: O(1)
function countSubstrings(s: string): number {
  // Treat each index as the center of potential palindromic substrings
  let cnt = 0;

  for (let i = 0; i < s.length; i++) {
    let start = i;
    let end = i;

    // Check for odd-length palindromes centered at i
    while (start >= 0 && end < s.length && s[start] === s[end]) {
      cnt++;
      start--; // <----
      end++; // ----->
    }

    // Check for even-length palindromes centered between i and i + 1
    start = i;
    end = i + 1;

    while (start >= 0 && end < s.length && s[start] === s[end]) {
      cnt++;
      start--;
      end++;
    }
  }

  return cnt;
}

// TC: O(n^2)
// SC: O(n^2)
/*
function countSubstrings(s: string): number {
  // dp[(start, end)] = s[start] === s[end] && dp[(start + 1, end - 1)]

  // A new starting character + an existing palindromic substring + a new ending character
  //        start                 dp[(start + 1, end - 1)]                 end

  const dp = new Map<string, boolean>();

  for (let end = 0; end < s.length; end++) {
    // start ranges from end down to 0
    for (let start = end; start >= 0; start--) {
      const key = `${start}-${end}`;
      if (start === end) {
        // "a"
        dp.set(key, true);
      } else if (start + 1 === end) {
        // "aa"
        dp.set(key, s[start] === s[end]);
      } else {
        const prevKey = `${start + 1}-${end - 1}`;
        dp.set(key, s[start] === s[end] && dp.get(prevKey) === true);
      }
    }
  }

  let cnt = 0;

  for (const [key, value] of dp.entries()) {
    if (value) {
      cnt++;
    }
  }

  return cnt;
}
*/

// TC: O(n^3)
// SC: O(1)
// function countSubstrings(s: string): number {
//   const isPalindromic = (left: number, right: number) => {
//     while (left < right) {
//       if (s[left] !== s[right]) return false;

//       left++;
//       right--;
//     }

//     return true;
//   };

//   let cnt = 0;

//   for (let i = 0; i < s.length; i++) {
//     for (let j = i; j < s.length; j++) {
//       if (isPalindromic(i, j)) {
//         cnt++;
//       }
//     }
//   }

//   return cnt;
// }
