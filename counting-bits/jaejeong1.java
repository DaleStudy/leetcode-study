class SolutionCountingBits {
  public int[] countBits(int n) {
    // 0 ~ n 까지의 수를 이진수로 변환한다음, 1의 개수를 카운트해 배열로 반환
    // 홀수/짝수 여부를 나눠서 1의 개수를 구함
    // 홀수: 이전 값 + 1, 짝수: i / 2의 1의 개수와 같은 값
    // 시간복잡도: O(N), 공간복잡도: O(N)

    int[] countingBits = new int[n + 1];
    countingBits[0] = 0;

    for (int i=1; i<=n; i++) {
      if (isOddNumber(i)) {
        countingBits[i] = countingBits[i - 1] + 1;
      } else {
        countingBits[i] = countingBits[i / 2];
      }
    }

    return countingBits;
  }

  // 시간복잡도: O(1)
  private boolean isOddNumber(int n) {
    return n % 2 == 1;
  }
}