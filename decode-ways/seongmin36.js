/**
검증해야되는 케이스는 총 2가지다.
1. 1~9까지의 알파벳
2. 10~26까지의 알파벳

우선 맨 앞자리가 '0'인 경우는 항상 0을 반환하도록 한다.
substring() 메서드를 활용하여 s로부터 특정 범위의 string을 가져와야 한다.
1자리일 때(one_char), 2자리일 때(two_char) 케이스를 비교한다.

중요한 점은 '비교한 값은 어떻게 저장해야하는가?'이다.
여러 방법이 있지만, 'climbing stairs'(피보나치 수열)에서 사용했던 '바텀업 방식의 DP'를 사용한다.
바텀업 DP를 사용하는 이유는 두 가지의 케이스의 합을 기억하고 더한 값을 가져와야하기 때문이다.
 */

/**
 * @param {string} s
 * @return {number}
 */
function numDecodings(s) {
  if (s[0] === "0") return 0;

  let dp = new Array(s.length + 1).fill(0);

  dp[0] = 1;

  function isAlphabet(str) {
    if (str.length === 1) return str >= "1" && str <= "9";
    if (str.length === 2) return str >= "10" && str <= "26";

    return false;
  }

  for (let i = 1; i < dp.length; i++) {
    let one_char = s.substring(i - 1, i);
    let two_char = s.substring(i - 2, i);

    if (isAlphabet(one_char)) {
      dp[i] += dp[i - 1];
    }
    if (i >= 2) {
      if (isAlphabet(two_char)) {
        dp[i] += dp[i - 2];
      }
    }
  }
  return dp[s.length];
}
