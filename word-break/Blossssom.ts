/**
 * @param s - 타겟 문자열
 * @param wordDict - 문자열 배열
 * @returns - wordDict의 요소를 조합해 타겟 문자열을 만들 수 있는지 return
 * @description
 * - wordDict의 요소는 중복 사용 가능
 * - dp 까진 생각했지만 세부 구현까진 힘들었음
 */

function wordBreak(s: string, wordDict: string[]): boolean {
  // 각 요소별 남은 단어를 저장한다면?
  const dictSet = new Set(wordDict);
  const dp = Array.from({ length: s.length + 1 }, () => false);

  dp[0] = true;

  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && dictSet.has(s.slice(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[s.length];
}

const s = "catsandog";
const wordDict = ["cats", "dog", "sand", "and", "cat"];

const answer = wordBreak(s, wordDict);
console.log("is answer :", answer);


