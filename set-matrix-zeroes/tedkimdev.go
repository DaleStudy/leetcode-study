// TC: O(m * n)
// SC: O(1)
func setZeroes(matrix [][]int) {
	rowNum, colNum := len(matrix), len(matrix[0])

	firstRowIsZero := false

	for r := 0; r < rowNum; r++ {
		for c := 0; c < colNum; c++ {
			if matrix[r][c] == 0 {
				matrix[0][c] = 0
				if r > 0 {
					matrix[r][0] = 0
				} else {
					firstRowIsZero = true
				}
			}
		}
	}

	for r := 1; r < rowNum; r++ {
		for c := 1; c < colNum; c++ {
			if matrix[r][0] == 0 || matrix[0][c] == 0 {
				matrix[r][c] = 0
			}
		}
	}

	if matrix[0][0] == 0 { // first column is zero
		for r := 0; r < rowNum; r++ {
			matrix[r][0] = 0
		}
	}

	if firstRowIsZero {
		for c := 0; c < colNum; c++ {
			matrix[0][c] = 0
		}
	}
}
