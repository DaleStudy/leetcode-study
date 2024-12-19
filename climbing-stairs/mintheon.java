class Solution {
  public int climbStairs(int n) {
    int[] stepCount = new int[n + 1];

    if(n == 1) {
      return 1;
    }

    stepCount[1] = 1;
    stepCount[2] = 2;
    for(int i = 3; i <= n; i++) {
      stepCount[i] = stepCount[i - 1] + stepCount[i - 2];
    }

    return stepCount[n];
  }
}