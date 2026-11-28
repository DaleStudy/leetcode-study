/*
시간 복잡도: O(n)
공간 복잡도: O(1)
풀이 기법: Dynamic Programming(Space Optimisation)
Self Feedback: 1트 째에는 아이디어를 완전히 떠올리지 못했고, 2트 째에는 구체적인 구현에서 막혔다. Space Optimisation과 점화식 부분은 캐치했음.
해설: 
(1) A-Z까지는 1-26의 범위의 값을 가진다.
(2) 각 해석할 수 있는 경우의 수를 쪼갤 수 있으며, 1글자 단위(1-9), 2글자 단위(10-26)로 나눌 수 있다.
(3) 점화식 역시 dp[n] = dp[n-1] + dp[n-2]
(4) 다만, 기존의 DP 문제와 완전히 동일한 건 아니다.
- s[0], 즉 "0126" 등의 무효한 코드값이 주어질 경우 무효 코드로 간주, 0을 반환해야 한다.
- dp[n-1]의 경우, 0이 아닌 글자의 경우 current += prev1하여 합산한다.
- dp[n-2]의 경우, parseInt로 쪼개어 2글자를 number 형태로 추출한다. 10~26 범위에 들어와있을 때 current += prev2한다.
- prev2 = prev1, prev1 = current로 점화식을 전개한다.
*/

const INVALID_CODE = "0"

function numDecodings(s: string): number {
  const n = s.length
  if (n === 0 || s[0] === INVALID_CODE) return 0

  //dp[n] = dp[n-1] + dp[n-2]
  let prev1 = 1 //dp[n-1]
  let prev2 = 1 //dp[n-2]

  for (let i = 2; i <= n; i++) {
    let current = 0
    // 1글자(Single Digit), dp[n-1]
    if (s[i - 1] !== INVALID_CODE) current += prev1

    // 2글자(Two Digit), dp[n-2]
    const twoDigit = parseInt(s.substring(i - 2, i))
    if (twoDigit >= 10 && twoDigit <= 26) {
      current += prev2
    }

    prev2 = prev1
    prev1 = current
  }

  return prev1
}
