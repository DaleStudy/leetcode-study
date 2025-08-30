import java.util.ArrayList;
import java.util.List;

public class Geegong {

    /**
     * direction vector 와 vistited 배열을 이용해 메모이제이션을 활용하여 풀어보기
     * time complexity : o(n)
     * space complexity : o(n) - result 용
     * @param matrix
     * @return
     */
    // move Colum direction , move Row Direction
    public int[][] directionVectors = {{0,1}, {1,0}, {0,-1}, {-1, 0}};
    public List<Integer> spiralOrder(int[][] matrix) {

        List<Integer> result = new ArrayList<>(matrix.length * matrix[0].length);

        // for memoization, 방문한 matrix의 인덱스들을 저장
        // int 배열은 기본으로 0 이 초기화
        int[][] visited = new int[matrix.length][matrix[0].length];

        makeSpiralMatrix(matrix, 0,0, 0, result, visited);

        return result;
    }

    public void makeSpiralMatrix(int[][] matrix, int startRowIdx, int startColIdx, int directionOrder, List<Integer> result, int[][] visited) {
        if (startRowIdx < 0 || startRowIdx >= matrix.length || startColIdx < 0 || startColIdx >= matrix[0].length) {
            return;
        }

        // 방문했던 녀석을 다시 찾아온거라면 다 돌았다고 판단하고 recursive 종료
        if (visited[startRowIdx][startColIdx] == 1) {
            return;
        }

        // 이번 순서의 vector 를 가져온다
        int[] direction = directionVectors[directionOrder];

        // row, col 각각 어떤 방향으로 움직일지 지정
        int moveRowPos = direction[0];
        int moveColPos = direction[1];

        int count = 0;

        int rowIndex = startRowIdx + (moveRowPos * count);
        int colIndex = startColIdx + (moveColPos * count);

        do {
            int currentVal = matrix[rowIndex][colIndex];
            result.add(currentVal);
            visited[rowIndex][colIndex] = 1;

            count++;
            rowIndex = startRowIdx + (moveRowPos * count);
            colIndex = startColIdx + (moveColPos * count);
            if (colIndex < 0 || colIndex >= matrix[0].length || rowIndex < 0 || rowIndex >= matrix.length) {
                break;
            }

        } while(visited[rowIndex][colIndex] != 1);

        // vector 리스트들은 0번째, 1번째, 2번째, 3번째, 0번째, 1번째 .. 이 순서대로 꺼내서 사용한다
        int nextDirectionOrder = directionOrder + 1 >= directionVectors.length ? 0 : directionOrder + 1;
        // 다음 방향을 미리 지정
        int[] nextDirection = directionVectors[nextDirectionOrder];

        // 다음 방향의 시작점 미리 지정
        count--;
        int nextStartRowIdx = startRowIdx + (moveRowPos * count) + nextDirection[0];
        int nextStartColIdx = startColIdx + (moveColPos * count) + nextDirection[1];

        makeSpiralMatrix(matrix, nextStartRowIdx, nextStartColIdx, nextDirectionOrder, result, visited);
    }
}



