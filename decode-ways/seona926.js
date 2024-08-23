/**
 * @param {string} s
 * @return {number}
 */
let numDecodings = function (s) {
  // 입력받은 숫자가 decode될 수 있는 가짓수를 리턴하기
  const n = s.length;
  if (n === 0) return 0;

  // dp[i]는 s[0...i-1]까지의 부분 문자열이 해석될 수 있는 방법의 수를 저장
  const dp = new Array(n + 1).fill(0);

  // 빈 문자열은 하나의 방법으로 해석될 수 있음 (아무것도 선택하지 않는 방법)
  dp[0] = 1;

  // 첫 글자가 '0'이 아니라면, 한 가지 방법으로 해석될 수 있음
  dp[1] = s[0] === "0" ? 0 : 1;

  for (let i = 2; i <= n; i++) {
    const oneDigit = parseInt(s.slice(i - 1, i)); // 마지막 한 글자
    const twoDigits = parseInt(s.slice(i - 2, i)); // 마지막 두 글자

    // 한 글자가 유효하다면, 그 글자를 포함하는 모든 방법을 추가
    if (oneDigit >= 1 && oneDigit <= 9) {
      dp[i] += dp[i - 1];
    }

    // 두 글자가 유효하다면, 그 두 글자를 포함하는 모든 방법을 추가
    if (twoDigits >= 10 && twoDigits <= 26) {
      dp[i] += dp[i - 2];
    }
  }

  return dp[n];
};

/*
  1. 시간복잡도 : O(n)
    - 반복문의 시간복잡도
  2. 공간복잡도 : O(n)
    - dp 배열의 공간 복잡도
*/
