var wordBreak = function (s, wordDict) {
  let memo = {};

  const dfs = (start) => {
    if (start in memo) return memo[start];

    if (start === s.length) {
      memo[start] = true;
      return true;
    }

    for (const word of wordDict) {
      if (s.substring(start, start + word.length) === word) {
        if (dfs(start + word.length)) {
          memo[start] = true;
          return true;
        }
      }
    }
    memo[start] = false;
    return false;
  };

  return dfs(0);
};

// n = s.length | m = wordDict.length | L = maximum length of word in wordDict
// TC: O(n*m*L)
// SC: O(n)
