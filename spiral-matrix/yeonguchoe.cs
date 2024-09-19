using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> SpiralOrder(int[][] matrix) {
        List<int> result = new List<int>();
        int row = matrix.Length;
        if (row == 0) return result;
        int column = matrix[0].Length;

        int upRail = 0;
        int downRail = row - 1;
        int leftRail = 0;
        int rightRail = column - 1;

        while (result.Count < row * column) {
            // L->R
            for (int c = leftRail; c <= rightRail; c++) {
                result.Add(matrix[upRail][c]);
            }
            // T->B
            for (int r = upRail + 1; r <= downRail; r++) {
                result.Add(matrix[r][rightRail]);
            }

            // R->L
            if (upRail != downRail) {
                for (int c = rightRail - 1; c >= leftRail; c--) {
                    result.Add(matrix[downRail][c]);
                }
            }

            // B->T
            if (leftRail != rightRail) {
                for (int r = downRail - 1; r > upRail; r--) {
                    result.Add(matrix[r][leftRail]);
                }
            }

            leftRail += 1;
            rightRail -= 1;
            upRail += 1;
            downRail -= 1;
        }

        return result;
    }
}
