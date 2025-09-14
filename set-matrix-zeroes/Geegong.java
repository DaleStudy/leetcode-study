import java.util.Arrays;

public class Geegong {


    /**
     * in-place 풀이여서 matrix 안에 0 으로 첫번째 row, column 에 0으로 채워야 하는 부분을 마킹해두는 식으로 풀이
     * time complexity : O(2MN) -> O(MN)
     * space complexity : O(1)
     * @param matrix
     */
    public void setZeroes(int[][] matrix) {

        // 가장 자리 top, left 에 1이 있는 지 체크
        // in-place 라고 풀었는데 가장 자리에 1이 있는지 체크는 변수 한두개 정도는 써도 되는듯..?
        boolean zeroExistsInTop = false;
        boolean zeroExistsInLeft = false;
        for (int colIndex=0; colIndex< matrix[0].length; colIndex++) {
            if (matrix[0][colIndex] == 0) {
                zeroExistsInTop = true;
                break;
            }
        }

        for (int rowIndex = 0; rowIndex < matrix.length; rowIndex++) {
            if (matrix[rowIndex][0] == 0) {
                zeroExistsInLeft = true;
                break;
            }
        }

        // 가장자리를 제외하고 안쪽에만 먼저 0으로 채워야되는 케이스들을 골라냄
        for (int rowIndex = 1; rowIndex < matrix.length; rowIndex++) {
            for (int colIndex=1; colIndex < matrix[0].length; colIndex++) {

                if (matrix[rowIndex][colIndex] == 0) {
                    matrix[0][colIndex] = 0;
                    matrix[rowIndex][0] = 0;
                }
            }
        }

        for (int rowIndex = 1; rowIndex < matrix.length; rowIndex++) {
            for (int colIndex = 1; colIndex < matrix[0].length; colIndex++) {
                if (matrix[0][colIndex] == 0 || matrix[rowIndex][0] == 0) {
                    matrix[rowIndex][colIndex] = 0;
                }
            }
        }

        if (zeroExistsInTop) {
            for (int colIndex=0; colIndex<matrix[0].length; colIndex++) {
                matrix[0][colIndex] = 0;
            }
        }

        if (zeroExistsInLeft) {
            for (int rowIndex=0; rowIndex<matrix.length; rowIndex++) {
                matrix[rowIndex][0] = 0;
            }
        }

    }
}

