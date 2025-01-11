// 시간 복잡도: O(N*N)
// 공간 복잡도: O(N*N)

// 이동하는 방향을 바꾸는 조건 (아래 중 하나 만족)
// 1. 다음에 갈 곳이 이미 방문한 곳
// 2. 다음에 갈 곳이 배열 범위를 벗어난 곳
class Solution {
	public List<Integer> spiralOrder(int[][] matrix) {
		int row = matrix.length;
		int col = matrix[0].length;
		boolean[][] visited = new boolean[row][col];

		// right, down, left, up
		int[] dirY = new int[]{1,0,-1,0}; // 열 방향
		int[] dirX = new int[]{0,1,0,-1}; // 행 방향
		int dirPointer = 0;

		List<Integer> result = new ArrayList<>();

		int x = 0, y = 0;
		int cnt = 0; int total = row*col;
		while(cnt < total){

			result.add(matrix[x][y]);
            visited[x][y]=true;
			++cnt;
			// 다음 좌표로 이동
			int nextX = x + dirX[dirPointer];
			int nextY = y + dirY[dirPointer];

			// 경계 조건 체크 및 방향 전환
			if (nextX < 0 || nextX >= row || nextY < 0 || nextY >= col || visited[nextX][nextY]) {
				// 현재 방향에서 벗어나면 방향을 변경
				dirPointer = (dirPointer + 1) % 4;
				nextX = x + dirX[dirPointer];
				nextY = y + dirY[dirPointer];
			}

			// 좌표 업데이트
			x = nextX;
			y = nextY;
		}


		return result;
	}
}
