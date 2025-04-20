// Approach 4:
// Time Complexity: O(n)
// ✅ Space Complexity: O(1)

function numDecodings(s: string): number {
  // s:   2 2 6
  // dp:    ? ? 1
  //       cur nxt

  let next = 0,
    current = 1;

  for (let start = s.length - 1; start >= 0; start--) {
    const temp = current;

    if (s[start] === "0") {
      // dp[start] = 0
      current = 0;
      next = temp;
    } else if (
      start + 1 < s.length &&
      parseInt(s.substring(start, start + 2)) < 27
    ) {
      // dp[start] = dp[start + 1] + dp[start + 2]
      current = current + next;
      next = temp;
    } else {
      // dp[start] = dp[start + 1]
      next = temp;
    }
  }
  return current;
}


// Approach 3: Dynamic Programming
// Time Complexity: O(n)
// Space Complexity: O(n)

// function numDecodings(s: string): number {
//   //    12
//   // dp 001
//   //    211

//   //    226
//   // dp 0001
//   //    3211

//   const dp = Array.from({ length: s.length + 1 }, (el) => 0);
//   dp[dp.length - 1] = 1;

//   for (let start = s.length - 1; start >= 0; start--) {
//     if (s[start] === "0") {
//       dp[start] = 0;
//     } else if (
//       start + 1 < s.length &&
//       parseInt(s.substring(start, start + 2)) < 27
//     ) {
//       dp[start] = dp[start + 1] + dp[start + 2];
//     } else {
//       dp[start] = dp[start + 1];
//     }
//   }

//   return dp[0];
// }


// Approach 2
// ✅ Time Complexity: O(2^n) -> O(n)
// Space Complexity: O(n)

// function numDecodings(s: string): number {
//   const memo = new Map<number, number>();
//   memo.set(s.length, 1);

//   const dfs = (start: number) => {
//     if (memo.has(start)) return memo.get(start);
//     if (s[start] === "0") {
//       memo.set(start, 0);
//     } else if (
//       start + 1 < s.length &&
//       parseInt(s.substring(start, start + 2)) < 27
//     ) {
//       memo.set(start, dfs(start + 1)! + dfs(start + 2)!);
//     } else {
//       memo.set(start, dfs(start + 1)!);
//     }
//     return memo.get(start);
//   };
//   return dfs(0)!;
// }


// Approach 1
// ❌ Time Limit Exceeded!
// Time Complexity: O(2^n), where n = s.length
// Space Compexity: O(n), due to recursive call stack
// function numDecodings(s: string): number {
//   const dfs = (start: number) => {
//     if (start === s.length) {
//       return 1;
//     }

//     if (s[start] === "0") {
//       return 0;
//     }

//     if (start + 1 < s.length && parseInt(s.substring(start, start + 2)) < 27) {
//       return dfs(start + 1) + dfs(start + 2);
//     } else {
//       return dfs(start + 1);
//     }
//   };

//   return dfs(0);
// }
