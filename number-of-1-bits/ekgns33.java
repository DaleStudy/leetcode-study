class Solution {
  public int hammingWeight(int n) {
    int curN = n;
    int cnt = 0;
    while(curN > 0) {
      if(curN %2 == 1) {
        cnt++;
      }
      curN /= 2;
    }
    return cnt;
  }
}
/**

 1 2 3 4 5 6 7 8 9 10 11
 0 1 2 1 2 2 3 1 2  2  3

 */
