class SolutionJaejeong1 {
  public int hammingWeight(int n) {
    // 주어진 양의 정수를 이진수로 변환하고, 1로 설정된 자릿수의 개수를 반환
    // 시간복잡도: O(1), 공간복잡도: O(1)
    int num = 0;
    for (int i=0; i<32; i++) {
      if((n & 1) == 1) {
        num++;
      }
      n = n >> 1;
    }
    return num;
  }
}
