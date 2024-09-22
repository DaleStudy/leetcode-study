class SolutionMaxArea {
  public int maxArea(int[] height) {
    // A와 B 간 면적 = (A와 B의 X축 차이) * (A와 B Y축 중 더 작은 Y축 길이)
    // 1번째 풀이 방법: 선택할 수 있는 모든 경우에 대해 위 값을 구한다, 시간복잡도: O(N^2) / 공간복잡도: O(1)
    // (최종) 2번째 풀이 방법: 양쪽 끝에서 투포인터로 좁혀오면서 면적을 구한다, 시간복잡도: O(N) / 공간복잡도: O(1)
    // 전체 너비를 고려하면서 움직여야한다.
    // 매번 면적을 계산하고, 더 크면 저장한다.
    // lt와 rt 중 더 낮은쪽을 좁힌다

    var lt = 0;
    var rt = height.length-1;
    var maxArea = 0;

    while(lt < rt) {
      var x = rt - lt;
      var y = Math.min(height[lt], height[rt]);
      var currentArea = x * y;
      if (maxArea < currentArea) {
        maxArea = currentArea;
      }

      if (height[lt] < height[rt]) {
        lt++;
      } else {
        rt--;
      }
    }

    return maxArea;
  }
}
