/*
* 조건
* 영어소문자로만 구성되어있음
* wordDict안에 있는 문자를 가지고 s를 만들 수 있으면 true return

* 아이디어
* wordDict안에 있는 단어들 중 s의 prefix 단어를 찾는다.
* prefix가 되는 단어를 뺀, 나머지 뒤의 문자열이 wordDict안에 있는 단어로 시작되는지 찾는다.
* 이 과정을 반복해서, s의 길이가 0이 되면 true를 리턴한다.
* wordDict안에 있는 단어를 다 조회해도 s가 남아있다면 false를 리턴한다.
*/

function wordBreak(s: string, wordDict: string[]): boolean {
  const memo: Record<string, boolean> = {};
  return isBreak(s, wordDict, memo);
}

function isBreak(s: string, wordDict: string[], memo: Record<string, boolean>) {
  if (s.length === 0) return true;
  if (s in memo) return memo[s];
  for (const word of wordDict) {
    const length = word.length;
    if (s.startsWith(word) && isBreak(s.slice(length), wordDict, memo)) {
      memo[s] = true;
      return true;
    }
  }

  memo[s] = false;
  return false;
}
// TC: O(s*w)
// SC: O(s)
// s: s.length, w: wordDict.length
