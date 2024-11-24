/*
풀이
- BFS를 이용하여 풀이할 수 있습니다
- 주어진 배열의 가장자리에서부터 시작하는 BFS를 pacific과 atlantic에 대해 각각 실행합니다

Big O
- M: 주어진 배열의 행의 개수
- N: 주어진 배열의 열의 개수
- Time complexity: O(MN)
  - 탐색을 진행하는 회수는 배열의 원소 개수에 비례하여 증가합니다
- Space complexity: O(MN)
  - queue의 최대 크기는 배열의 원소 개수에 비례하여 증가합니다
  - memo 배열의 크기는 배열의 원소 개수에 비례하여 증가합니다
*/

type pair struct {
	pacific  bool
	atlantic bool
}

func pacificAtlantic(heights [][]int) [][]int {
	var res [][]int

	m, n := len(heights), len(heights[0])

	dr := []int{0, 0, 1, -1}
	dc := []int{1, -1, 0, 0}

	// 모든 r, c에 대해 memo[r][c] = {pacific: false, atlantic: false}로 초기화합니다
	memo := make([][]pair, m)
	for r := range memo {
		memo[r] = make([]pair, n)
	}

	queue := make([][]int, 0)

	// pacific에서 시작하는 BFS
	for c := 0; c < n; c++ {
		queue = append(queue, []int{0, c})
	}
	for r := 1; r < m; r++ {
		queue = append(queue, []int{r, 0})
	}

	for len(queue) > 0 {
		r, c := queue[0][0], queue[0][1]
		queue = queue[1:]

		memo[r][c].pacific = true

		for i := 0; i < 4; i++ {
			nr, nc := r+dr[i], c+dc[i]

			if !(0 <= nr && nr < m && 0 <= nc && nc < n) {
				continue
			}

			if heights[r][c] <= heights[nr][nc] && !memo[nr][nc].pacific {
				queue = append(queue, []int{nr, nc})
			}
		}
	}

	// atlantic에서 시작하는 BFS
	for c := 0; c < n; c++ {
		queue = append(queue, []int{m - 1, c})
	}
	for r := 0; r < m-1; r++ {
		queue = append(queue, []int{r, n - 1})
	}

	for len(queue) > 0 {
		r, c := queue[0][0], queue[0][1]
		queue = queue[1:]

		memo[r][c].atlantic = true

		for i := 0; i < 4; i++ {
			nr, nc := r+dr[i], c+dc[i]

			if !(0 <= nr && nr < m && 0 <= nc && nc < n) {
				continue
			}

			if heights[r][c] <= heights[nr][nc] && !memo[nr][nc].atlantic {
				memo[nr][nc].atlantic = true
				queue = append(queue, []int{nr, nc})
			}
		}
	}

	for r, row := range memo {
		for c, el := range row {
			if el.pacific && el.atlantic {
				res = append(res, []int{r, c})
			}
		}
	}

	return res
}
