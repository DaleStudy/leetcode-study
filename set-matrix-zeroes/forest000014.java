/*
solution 1. 재귀 호출
Time Complexity: O(m * n * (m + n))
Space Complexity: O(m * n)
처음에는 공간 복잡도를 O(1)이라고 생각했으나, 검색해보니 함수 호출 스택도 공간 복잡도 계산에 포함시켜야만 한다. 따라서 이 방법은 공간 복잡도 제한을 만족시키지 못한다.
(참고 : https://en.wikipedia.org/wiki/In-place_algorithm), 


solution 2. bit manipulation

long 변수를 선언해서, 각 bit에 x번째 row(혹은 col)를 0으로 바꿀지 여부를 기록한다.
(m + n) / 64 개의 변수를 써서 가능하긴 하지만, 64라는 factor가 다소 클 뿐, 결국 공간 복잡도는 O(m + n).


solution 3. matrix 내에 안 쓰이는 값 찾기 (probabilistic 접근)
int32 범위 내에서, 쓰이는 값보다는 안 쓰이는 값의 갯수가 압도적으로 많다.(99.999%+)

int 범위 내의 숫자를 랜덤하게 뽑는다면, 그리고 이 행위를 10번만 반복한다면 
O(m * n) 시간에 상당히 높은 확률로 안 쓰이는 값(x라고 하자)을 찾을 수 있다.
(틀릴 확률은 10^(-50) 정도.)
matrix의 모든 원소를 순회하며, 값이 0이라면 같은 row/col에 존재하는 모든 원소(또다른 0은 제외)를 위에서 찾은 x로 바꾼 뒤에, 마지막에 한번에 모든 x를 0으로 바꾸는 식으로 풀 수 있다.

그러나 이 접근법의 확률은 문제의 제한 조건 m, n 범위 하에서 계산한 것이라는 한계가 있다.
m, n이 꽤나 커진다면 맞출 확률이 낮아지고, 극단적으로 m = n = 2^16 = 65,536 이상이 되면, 쓸 수 없는 방법이기도 하다.


solution 4. in-place marking
(AlgoDale 풀이를 참고함)
Time Complexity: O(m * n)
Space Complexity: O(1)

*/
class Solution {

    // solution 4. in-place marking
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        boolean should0thColumnBeZero = false;
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                should0thColumnBeZero = true;
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < m; i++) {
            if (matrix[i][0] == 0) {
                for (int j = 1; j < n; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int i = 1; i < n; i++) {
            if (matrix[0][i] == 0) {
                for (int j = 0; j < m; j++) {
                    matrix[j][i] = 0;
                }
            }
        }
        if (matrix[0][0] == 0) {
            for (int i = 0; i < n; i++) {
                matrix[0][i] = 0;
            }
        }
        if (should0thColumnBeZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }

    /* solution 1. 재귀 호출
    public void setZeroes(int[][] matrix) {
        dfs(matrix, 0, 0);
    }

    public void dfs(int[][] matrix, int sr, int sc) {
        int m = matrix.length;
        int n = matrix[0].length;
        for (int r = sr; r < m; r++) {
            boolean found = false;
            for (int c = (r == sr) ? sc : 0; c < n; c++) {
                if (matrix[r][c] != 0) {
                    continue;
                }

                int nr = (c == n) ? (r + 1) : r;
                int nc = (c == n) ? 0 : c + 1;
                dfs(matrix, nr, nc);
                setRowAndColumnZeroes(matrix, r, c);
                
                found = true;
                break;
            }
            if (found) {
                break;
            }
        }
    }

    public void setRowAndColumnZeroes(int[][] matrix, int r, int c) {
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 0; i < n; i++) {
            matrix[r][i] = 0;
        }
        for (int i = 0; i < m; i++) {
            matrix[i][c] = 0;
        }
    }
    */
}
