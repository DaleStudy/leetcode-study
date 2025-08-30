// Time Complexity: O(m+n), m: matrix.length, n: matrix[0].length
// Space Complexity: O(m*n), m: matrix.length, n: matrix[0].length, because of arraylist for output
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int rowMin = 0;
        int rowMax = matrix.length-1;
        int colMin = 0;
        int colMax = matrix[0].length-1;

        ArrayList<Integer> orderedElements = new ArrayList<>();

        while (rowMin <= rowMax && colMin <= colMax) {
            // left to right
            for (int col = colMin; col <= colMax; ++col) {
                orderedElements.add(matrix[rowMin][col]);
            }
            rowMin++;

            // top to bottom
            for (int row = rowMin; row <= rowMax; ++row) {
                orderedElements.add(matrix[row][colMax]);
            }
            colMax--;

            // right to left
            if (rowMin <= rowMax) {
                for (int col = colMax; col >= colMin; --col) {
                    orderedElements.add(matrix[rowMax][col]);
                }
            }
            rowMax--;

            // bottom to top
            if (colMin <= colMax) {
                for (int row = rowMax; row >= rowMin; --row) {
                    orderedElements.add(matrix[row][colMin]);
                }
            }
            colMin++;
        }

        return orderedElements;
    }
}
