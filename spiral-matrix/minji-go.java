/**
 * <a href="https://leetcode.com/problems/spiral-matrix/">week06-5.spiral-matrix</a>
 * <li>Description: return all elements of the matrix in spiral order</li>
 * <li>Topics: Array, Matrix, Simulation        </li>
 * <li>Time Complexity: O(N*M), Runtime 0ms     </li>
 * <li>Space Complexity: O(1), Memory 41.95MB   </li>
 */
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> answer = new ArrayList<>();
        int lr = 0;
        int hr = matrix.length-1;
        int lc = 0;
        int hc = matrix[0].length-1;

        while (lr<=hr && lc<=hc) {
            for(int c=lc; c<=hc && lr<=hr; c++) {
                answer.add(matrix[lr][c]);
            }
            lr++;

            for(int r=lr; r<=hr && lc<=hc; r++) {
                answer.add(matrix[r][hc]);
            }
            hc--;

            for(int c=hc; c>=lc && lr<=hr; c--){
                answer.add(matrix[hr][c]);
            }
            hr--;

            for(int r=hr; r>=lr && lc<=hc; r--){
                answer.add(matrix[r][lc]);
            }
            lc++;
        }
        return answer;
    }
}
