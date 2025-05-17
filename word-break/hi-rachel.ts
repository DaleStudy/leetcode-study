// wordDict 조합으로 s를 만들 수 있는지 반환해라
// TC: O(n^2) SC: O(n + m * k) => s의 길이 + (단어 수 * 평균 단어 길이)
// .has(word) => O(1)

function wordBreak(s: string, wordDict: string[]): boolean {
  const wordSet = new Set(wordDict);
  const dp: boolean[] = Array(s.length + 1).fill(false);
  dp[0] = true;

  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && wordSet.has(s.slice(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[s.length];
}

// PY 풀이
// class Solution:
//     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
//         wordSet = set(wordDict)
//         dp = [False] * (len(s)+1)
//         dp[0] = True

//         for i in range(1, len(s)+1):
//             for j in range(0, i):
//                 if dp[j] and s[j:i] in wordSet:
//                     dp[i] = True

//         return dp[len(s)]
