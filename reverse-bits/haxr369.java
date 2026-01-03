class Solution {
  /**
   * Runtime: 1 ms (Beats 54.22%)
   * Memory: 42.34 MB (Beats 63.68%)
   * Space Complexity: O(1)
   * > 고정된 32byte 배열 사용으로 O(1)
   * Time Complexity: O(logN)
   * - n의 2진수 변환 => O(logN)
   * - 32bit 역순 변환 => O(1)
   * > O(log32) + O(1) => O(log32) 사실상 O(1)
   * 
   */
  public int reverseBits(int n) {
    byte[] binarys = new byte[32];
    int temp = n;

    // n의 2진수를 저장하기
    int i = 0;
    while (temp > 0) { // 최종 0이되면 종료
      // 짝수인 경우 i번째 비트는 0
      if (temp % 2 == 0) {
        binarys[i] = 0;
      } else { // 홀수면 i번째 비트는 1
        binarys[i] = 1;
        temp -= 1;
      }
      temp = temp / 2;
      i++; // 비트수 올리기
    }

    // 저장된 비트를 역순으로 십진수로 변환하기
    int ans = 0; // 총합산
    int base = 1; // i-j번째 2진수 값
    int j = 0;
    while (31 >= j) {
      // 2진수가 1인 경우만 합산한다.
      if (binarys[31 - j] == 1) {
        ans += base;
      }
      base *= 2;
      j++;
    }
    return ans;
  }
}
