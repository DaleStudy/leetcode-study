/**
 * 시간 복잡도 O(n)
 * 공간 복잡도 O(1)
 */
function numDecodings(s: string): number {
  const n = s.length;
  if (n === 0 || s[0] === "0") return 0;

  // prev2 = dp[i-2], prev1 = dp[i-1]
  let prev2 = 1; // dp[0]
  let prev1 = 1; // dp[1] (s[0]이 '0'이 아님을 위에서 보장)

  for (let i = 2; i <= n; i++) {
    let cur = 0;
    const one = s[i - 1]; // 마지막 한 자리
    const two = Number(s.slice(i - 2, i)); // 마지막 두 자리

    if (one !== "0") cur += prev1; // 한 자리로 끊기
    if (two >= 10 && two <= 26) cur += prev2; // 두 자리로 끊기

    prev2 = prev1;
    prev1 = cur;
  }
  return prev1;
}
