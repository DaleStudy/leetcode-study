/**
  * TC : O(m * n)
  *   - matrix의 원소 수 m * n 만큼 순회 하므로 O(m * n)
  * SC : O(m * n)
  *   - matrix의 원소 수 m * n 만큼의 리스트를 생성하므로 O(m * n)
  */
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int[] dRow = {0, 1, 0, -1};
        int[] dCol = {1, 0, -1, 0};
    
        int direction = 0;
        List<Integer> list = new ArrayList<>();

        int rowCount = matrix.length;
        int colCount = matrix[0].length;

        int row = 0, col = 0;
        int totalElements = rowCount * colCount;

        for (int i = 0; i < totalElements; i++) {
            list.add(matrix[row][col]);
            matrix[row][col] = 101; // 방문 처리 (제약조건: -100 <= val <= 100)

            int nextRow = row + dRow[direction];
            int nextCol = col + dCol[direction];

            // 범위를 벗어나거나 이미 방문한 칸인 경우 방향 전환
            if (nextRow < 0 || nextRow >= rowCount || 
                nextCol < 0 || nextCol >= colCount || 
                matrix[nextRow][nextCol] > 100) {
                
                direction = (direction + 1) % 4;
            }

            row += dRow[direction];
            col += dCol[direction];
        }
        return list;
    }
}