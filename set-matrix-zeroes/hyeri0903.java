class Solution {
    public void setZeroes(int[][] matrix) {
        /**
        1.문제: 0이 존재하는 위치의 모든 row, column을 0으로 set
        2.constraints: 
        - m,n min = 1, max = 200
        - space: O(mn)으로 풀이하지말 것,
        3.solution
        - 0의 위치를 확인 -> 0의 위치는 여러개일 수 있음
        - row, col 각각 0의 위치 저장 
        - time: O(mn), space O(m+n)
         */
        int m = matrix.length;
        int n = matrix[0].length;
        int[] row = new int[m]; //0이 존재하는 row 위치이면 1, 아니면 0
        int[] col = new int[n]; //0이 존재하는 col 위치이면 1, 아니면 0

        int x = 0; int y = 0; //0의 위치

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(matrix[i][j] == 0) {
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(row[i] == 1 || col[j] == 1) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
