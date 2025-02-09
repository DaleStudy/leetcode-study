/*
*.      lr ->
*   ^   1 2 3 4. rd
*   lu  5 6 7 8. v
*        <-  rl
* tc : O(mn)
* sc : O(1)
* */

class Solution {
  public List<Integer> spiralOrder(int[][] matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    int lr = 0, rd = 0, rl = n -1, lu = m - 1;
    int cnt = 0, target = m*n;
    List<Integer> res = new ArrayList<>();

    while(lr <= rl && rd <= lu) {
      for(int startLeft = lr; startLeft <= rl; startLeft++) {
        res.add(matrix[rd][startLeft]);
      }
      rd++;
      for(int startUp = rd; startUp <=lu; startUp++) {
        res.add(matrix[startUp][rl]);
      }
      rl--;
      if(rd <= lu) {
        for(int startRight = rl; startRight >= lr; startRight--) {
          res.add(matrix[lu][startRight]);
        }
      }
      lu--;
      if(lr <= rl) {
        for(int startDown = lu; startDown >= rd; startDown--) {
          res.add(matrix[startDown][lr]);
        }
      }
      lr++;
    }
    return res;
  }
}
