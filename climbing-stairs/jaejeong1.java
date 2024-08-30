class SolutionClimbStairs {

  public int climbStairs(int n) {
    // n번째 계단까지 오르는 방법의 수
    // 첫 번째 계단까지 오르는 방법은 1가지
    // 두 번째 계단까지 오르는 방법은 2가지
    // 세 번째 계단부터는 이전 두 계단의 방법을 더하여 계산
    // stairs[i]는 i번째 계단까지 오르는 방법의 수
    // 시간복잡도: O(N), 공간복잡도: O(N)
    if (n == 1) {
      return 1;
    }

    if (n == 2) {
      return 2;
    }

    int[] stairs = new int[n+1];
    stairs[1] = 1;
    stairs[2] = 2;


    for (int i=3; i<=n; i++) {
      stairs[i] = stairs[i-1] + stairs[i-2];
    }

    return stairs[n];
  }
}
