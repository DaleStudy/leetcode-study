class Solution {
    /**
    1. understanding
    - iterate over all cells, if value is 0, then add row and col to sweep target set.
    - for each row target set, and col target set, sweep all it's value to 0
    2. complexity
    - time: O(m * n)
    - space: O(m + n)
     */
    public void setZeroes(int[][] matrix) {
        Set<Integer> rows = new HashSet<>(); // O(m)
        Set<Integer> cols = new HashSet<>(); // O(n)

        for (int row = 0; row < matrix.length; row++) { // O(m)
            for (int col = 0; col < matrix[row].length; col++) { // O(n)
                if (matrix[row][col] == 0) { // O(m * n)
                    rows.add(row);
                    cols.add(col);
                }
            }
        }

        for (int row: rows) { // O(m)
            int col = 0;
            while (col < matrix[row].length) { // O(n)
                matrix[row][col] = 0;
                col++;
            }
        }

        for (int col: cols) { // O(n)
            int row = 0;
            while (row < matrix.length) { // O(m)
                matrix[row][col] = 0;
                row++;
            }
        }
    }
}

