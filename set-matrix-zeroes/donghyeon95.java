class Solution {
	public void setZeroes(int[][] matrix) {
		int rows = matrix.length;
		int cols = matrix[0].length;

		boolean firstRowHasZero = false;
		boolean firstColHasZero = false;

		// 1. 첫 번째 행과 열에 0이 있는지 확인
		for (int i = 0; i < rows; i++) {
			if (matrix[i][0] == 0) {
				firstColHasZero = true;
				break;
			}
		}
		for (int j = 0; j < cols; j++) {
			if (matrix[0][j] == 0) {
				firstRowHasZero = true;
				break;
			}
		}

		// 2. 나머지 행렬에서 0 찾기 (첫 번째 행과 열에 기록)
		for (int i = 1; i < rows; i++) {
			for (int j = 1; j < cols; j++) {
				if (matrix[i][j] == 0) {
					matrix[i][0] = 0; // 해당 행 표시
					matrix[0][j] = 0; // 해당 열 표시
				}
			}
		}

		// 3. 첫 번째 행과 열의 정보를 기반으로 행렬 수정
		for (int i = 1; i < rows; i++) {
			for (int j = 1; j < cols; j++) {
				if (matrix[i][0] == 0 || matrix[0][j] == 0) {
					matrix[i][j] = 0;
				}
			}
		}

		// 4. 첫 번째 열 복구
		if (firstColHasZero) {
			for (int i = 0; i < rows; i++) {
				matrix[i][0] = 0;
			}
		}

		// 5. 첫 번째 행 복구
		if (firstRowHasZero) {
			for (int j = 0; j < cols; j++) {
				matrix[0][j] = 0;
			}
		}
	}
}


