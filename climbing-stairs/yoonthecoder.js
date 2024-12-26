function climbStairs(n) {
  // if there's only 1 step, return 1
  if (n === 1) return 1;
  // initialize the first prev values (when n=1 and n=0 each)
  let prev1 = 1;
  let prev2 = 1;
  // iterate through step 2 to n
  for (let i = 2; i <= n; i++) {
    let current = prev1 + prev2;
    prev2 = prev1;
    prev1 = current;
  }
  return prev1;
}

// Time complexity: O(n) - single for loop
// Space Complexity: O(1)
