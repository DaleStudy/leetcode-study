/*
풀이
- matrix를 4사분면으로 나눕니다
  1사분면의 모든 좌표에 대해 아래와 같은 연산을 수행합니다
- 1사분면의 좌표 a1에 대해 a2, a3, a4를 아래처럼 정의합니다
  a2: a1을 90도 회전시켰을 때의 좌표 (2사분면에 위치함)
  a3: a2를 90도 회전시켰을 때의 좌표 (3사분면에 위치함)
  a4: a3을 90도 회전시켰을 때의 좌표 (4사분면에 위치함)
  a1 -> a2, a2 -> a3, a3 -> a4, a4 -> a1으로 값을 변경시킵니다
Big O
- N: 매트릭스의 크기
- Time complexity: O(N^2)
- Space complexity: O(1)
*/

func rotate(matrix [][]int) {
	n := len(matrix)
	// 사분면의 크기, qr, qc: 사분면의 행, 열 크기
	qr := n / 2
	qc := (n + 1) / 2

	for r := 0; r < qr; r++ {
		for c := 0; c < qc; c++ {
			r1 := r
			c1 := c

			r2 := c
			c2 := n - 1 - r

			r3 := n - 1 - r
			c3 := n - 1 - c

			r4 := n - 1 - c
			c4 := r

			matrix[r1][c1], matrix[r2][c2], matrix[r3][c3], matrix[r4][c4] = matrix[r4][c4], matrix[r1][c1], matrix[r2][c2], matrix[r3][c3]
		}
	}
}
