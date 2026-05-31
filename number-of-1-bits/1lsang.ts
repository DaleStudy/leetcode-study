function hammingWeight(n: number): number {
  // 최대 이진수 찾기
  let s = 1;
  while (s*2 <= n) {
    s*=2;
  }

  // bit 세기
  let cnt = 0;
  while (n > 0) {
    if (n - s >= 0) {
      n -= s;
      cnt++;
    }
    s /= 2;
  }
  return cnt;
};
