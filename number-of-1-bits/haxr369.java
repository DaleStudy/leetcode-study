class Solution {
  /**
   * 주어진 숫자 n을 2진수로 만들고, 거기에 포함되는 1의 개수를 카운트하자.
   * 
   * 원리: 2진수에서 1의 의미.
   * 특정 수 M이 2^k <= M < 2^(k+1)의 관계를 가질 때,
   * M이 2^k로 나눠떨어진다면 k번째 bit는 1로 표현할 수 있다.
   * Runtime: 1 ms (Beats 18.72%)
   * Memory: 42.17 MB (Beats 24.03%)
   * Space Complexity: O(1)
   * - 2의 제곱수 v와 k를 저장하는 공간 => O(1)
   * > O(1)
   * Time Complexity: O(N)
   * - 30회의 n와 v의 비교 및 나눔셈 => O(31)
   * > O(31) => O(1)
   */
  public int hammingWeight(int n) {
    int ans = 0;

    int maxExponatial = 1 << 30;
    // n >= 2^30일 때 수를 줄이기
    if (maxExponatial <= n) {
      n = n - maxExponatial;
      ans++; // 2^31 사용했기에 1bit 추가
    }

    int k = 29;
    int v = 1 << 29;

    // 총 30번 돌기
    while (k >= 0) {
      // v <= n 일 때, k번째 bit는 1이다.
      if (v <= n) {
        n -= v;
        ans++;
      }
      // 항상 k와 v를 줄이기.
      k--;
      v = v >> 1;
    }
    return ans;

  }
}
