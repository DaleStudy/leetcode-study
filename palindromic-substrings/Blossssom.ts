/**
 * @param s - 문자열
 * @returns - 회문 (뒤집어 읽어도 같은 문자열) 의 갯수 반환
 * @description
 * - 같은 글자여도 각각은 따로 판단하며 한 글자도 회문으로 판단
 */

function countSubstrings(s: string): number {
  let n = s.length;
  let cnt = 0;
  const dp: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));

  for (let j = 0; j < s.length; j++) {
    for (let i = 0; i <= j; i++) {
      if (s[i] === s[j] && (j - i <= 2 || dp[i + 1][j - 1])) {
        dp[i][j] = true;
        cnt++;
      }
    }
  }
  return cnt;
}

const s = "aaa";
countSubstrings(s);


