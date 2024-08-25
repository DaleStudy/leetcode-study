/**
 * @description
 * time complexity: O(N^3)
 * space complexity: O(N)
 *
 * brainstorming:
 * 1. stack, permutation
 * 2. Brute force
 *
 * strategy:
 * Brute force, calculate
 *
 * reason:
 * intuitive way
 *
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
  let answer = 0;
  const len = s.length;

  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len + 1; j++) {
      const subStr = s.slice(i, j);
      if (isPalindrome(subStr)) answer++;
    }
  }

  return answer;
};

function isPalindrome(str) {
  const len = str.length;
  const middleIndex = Math.floor(len / 2);

  for (let i = 0; i < middleIndex; i++) {
    if (str[i] !== str[len - 1 - i]) return false;
  }

  return true;
}

/**
 * @description
 * time complexity: O(N^2)
 * space complexity: O(N^2)
 *
 * brainstorming:
 * 1. https://sbslc.tistory.com/56
 *
 * strategy:
 * dynamic programming
 *
 * reason:
 * to challenge dp
 *
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
  const answer = [];
  const MAX_LENGTH = s.length;
  const dp = Array.from({ length: MAX_LENGTH }, (_, i) =>
    Array.from({ length: MAX_LENGTH }, (_, j) => {
      if (i === j) answer.push(s[i]);
      return i === j;
    })
  );
  // Check next step ex) aa, bb, cc
  for (let i = 0; i < MAX_LENGTH - 1; i++) {
    const nextIndex = i + 1;
    if (s[i] === s[nextIndex]) {
      dp[i][nextIndex] = true;
      answer.push(s.slice(i, nextIndex + 1));
    }
  }
  // Check against values calculated in the previous step
  for (let len = 2; len <= MAX_LENGTH; len++) {
    for (let i = 0; i < MAX_LENGTH - len; i++) {
      const lastIndex = len + i;
      if (s[i] === s[lastIndex] && dp[i + 1][lastIndex - 1]) {
        dp[i][lastIndex] = true;
        answer.push(s.slice(i, lastIndex + 1));
      }
    }
  }

  return answer.length;
};
