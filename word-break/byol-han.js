/**
 * https://leetcode.com/problems/word-break/
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const wordSet = new Set(wordDict);
  const dp = new Array(s.length + 1).fill(false);
  dp[0] = true; // 빈 문자열은 항상 true

  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && wordSet.has(s.substring(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[s.length];
};

/*
Set은 검색이 빠르다
wordDict가 배열이면, includes()로 단어가 있는지 찾을 때 O(n) 시간이 걸림
하지만 Set을 사용하면 has() 메서드로 단어가 있는지 O(1) 시간이 걸림
이 차이는 s.length가 길거나 wordDict가 클수록 성능에 큰 영향
*/
