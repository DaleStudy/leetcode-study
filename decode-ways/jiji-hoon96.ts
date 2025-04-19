function numDecodings(s: string): number {
  // 빈 문자열이거나 0으로 시작하면 디코딩 불가
  if (!s || s[0] === '0') return 0;
  
  const n = s.length;
  
  // 문자열 길이가 1이면 바로 결과 반환
  if (n === 1) return 1;
  
  // 초기 상태
  let prev = 1;  // dp[0]
  let curr = s[0] === '0' ? 0 : 1;  // dp[1]
  
  for (let i = 2; i <= n; i++) {
      let temp = 0;
      const oneDigit = parseInt(s[i - 1]);
      const twoDigit = parseInt(s[i - 2] + s[i - 1]);
      
      // 한 자리 숫자로 디코딩 (1-9)
      if (oneDigit >= 1) {
          temp += curr;
      }
      
      // 두 자리 숫자로 디코딩 (10-26)
      if (twoDigit >= 10 && twoDigit <= 26) {
          temp += prev;
      }
      
      // 상태 업데이트
      prev = curr;
      curr = temp;
  }
  
  return curr;
}
