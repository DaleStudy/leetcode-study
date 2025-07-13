class Solution {

    // 공간복잡도 개선 및 별도의 방문 배열 처리 등 하지 않기 위해
    // 2nd solution
    public void rotate(int[][] matrix) {

        int n = matrix.length;

        // 행, 열 자리 바꾸기
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // 열 자리 swap 하기 
        // ex) 3 X 3 => 0 <-> 2 열 스왑
        // ex) 4 x 4 => 0 <-> 3, 1 <-> 2 스왑
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }


    // public void rotate(int[][] matrix) {

    // [0, 0], [0, 1], [0, 2]     [2, 0], [1, 0], [0, 0]
    // [1, 0], [1, 1], [1, 2]     [2, 1], [1, 1], [0, 1]
    // [2, 0], [2, 1], [2, 2]     [2, 2], [2, 1], [0, 2]


    // [0, 0], [0, 1], [0, 2], [0, 3]    [3, 0], [2, 0], [1, 0], [0, 0]
    // [1, 0], [1, 1], [1, 2], [1, 3]    [3, 1], [2, 1], [1, 1], [0, 1]
    // [2, 0], [2, 1], [2, 2], [2, 3]    [3, 2], [2, 2], [1, 2], [0, 2]
    // [3, 0], [3, 1], [3, 2], [3, 3]    [3, 3], [2, 3], [1, 3], [0, 3]

    // 90D =>
    // n = matrix.length이고 m = matrix[0].length일 때
    // 1 => 3 matrix[0][0] => matrix[0][2]
    // 2 => 6 matrix[0][1] => matrix[1][2]
    // 3 => 9 matrix[0][2] => matrix[2][2]
    // matrix[i][j] => matrix[j][n - 1 - i]

    //     int n = matrix.length;
    //     int m = matrix[0].length;

    //     boolean[][] visited = new boolean[n][m];

    //     for (int i = 0; i < n; i++) {
    //         for (int j = 0; j < m; j++) {                
    //             if (visited[i][j]) {
    //                 continue;
    //             }
    //             int temp = matrix[i][j];
    //             matrix[i][j] = matrix[j][n - 1 - i];
    //             matrix[j][n - 1 - i] = temp;

    //             visited[i][j] = true;
    //             visited[j][n - 1 - i] = true;      
    //         }            
    //     }
    // }
}

