/*
Big O
- N: 주어진 배열 intervals의 길이
- Time complexity: O(NlogN)
  - intervals를 start의 오름차순으로 정렬 -> O(NlogN)
  - 반복문 -> O(N)
  - O(NlogN + N) = O(NlogN)
- Space complexity: O(N)
  - 정답 배열의 크기 -> O(N)
*/

import "sort"

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	res := make([][]int, 0)
	start := intervals[0][0]
	end := intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		curr := intervals[i]
		if end >= curr[0] {
			end = max(end, curr[1])
		} else {
			res = append(res, []int{start, end})
			start = curr[0]
			end = curr[1]
		}
	}
	res = append(res, []int{start, end})
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
