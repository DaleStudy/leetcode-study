public class Solution {
  /**
   시간복잡도: O(1) -> 루프는 항상 32번 반복되기 때문
   공간복잡도: O(1)
   */

  // you need treat n as an unsigned value
  public int reverseBits(int n) {
    int answer = 0;
    int index = 31;

    while(n != 0) {
      // n&1 : 마지막 비트를 추출
      // << : 0을 패딩처리 시켜서 상위 자리수로 올려버림
      answer += (n & 1) << index;

      // >>> : 부호 상관없이 오른쪽으로 비트 이동
      n = n >>> 1;
      index--;
    }

    return answer;
  }
}
