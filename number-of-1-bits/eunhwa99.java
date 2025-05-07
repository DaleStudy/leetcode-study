// 시간 복잡도 O(log n) - n은 주어진 정수
// 공간 복잡도 O(1) - 상수 공간 사용
class Solution{
  public int hammingWeight(int n) {
    int count = 0;
    while (n != 0) {
      count += (n & 1); // 마지막 비트가 1인지 확인
      n >>= 1; // 오른쪽으로 비트 이동
    }
    return count;
  }
}

