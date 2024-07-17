// Time Complexity: O(n)
// Space Complexity: O(1)

var numDecodings = function (s) {
  const n = s.length;

  // if the string is empty or starts with '0', it cannot be decoded
  if (n === 0 || s[0] === "0") return 0;

  // initialize variables to store and decode up to the previous and the current index
  // corresponds to dp[i-1]
  let prev1 = 1;
  // corresponds to dp[i-2]
  let prev2 = 1;

  // iterate through the string from the second character onwards
  for (let i = 1; i < n; i++) {
    let current = 0;

    // single digit decoding
    let oneDigit = parseInt(s.substring(i, i + 1));
    if (oneDigit >= 1 && oneDigit <= 9) {
      current += prev1;
    }

    // two digit decoding
    let twoDigits = parseInt(s.substring(i - 1, i + 1));
    if (twoDigits >= 10 && twoDigits <= 26) {
      current += prev2;
    }

    // update prev2 and prev1 for the next iteration
    prev2 = prev1;
    prev1 = current;
  }

  // the way to decode the entire string, stored in prev1
  return prev1;
};
