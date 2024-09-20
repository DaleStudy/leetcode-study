class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> output = new ArrayList<>();
        int north = 0;
        int south = matrix.length - 1;
        int east = matrix[0].length - 1;
        int west = 0;

        while (north <= south && west <= east) {
            int j = west;
            while (j <= east) {
                output.add(matrix[north][j]);
                j += 1;
            }
            north += 1;

            int i = north;
            while (i <= south) {
                output.add(matrix[i][east]);
                i += 1;
            }
            east -= 1;

            if (north <= south) {
                j = east;
                while (j >= west) {
                    output.add(matrix[south][j]);
                    j -= 1;
                }
                south -= 1;
            }

            if (west <= east) {
                i = south;
                while (i >= north) {
                    output.add(matrix[i][west]);
                    i -= 1;
                }
                west += 1;
            }
        }
        return output;
    }
}
