/*
풀이
- 정렬 후 각 interval을 비교하여 풀 수 있습니다
Big O
- N: intervals의 길이
- Time complexity: O(NlogN)
  - sort.Slice -> average O(NlogN)
  - 두 번째 for -> O(N)
- Space complexity: O(logN)
  - golang의 sort package는 pdqsort를 사용합니다 -> O(logN)
    퀵소트의 재귀 호출 스택 깊이를 고려하여야 합니다
*/

import "sort"

func canAttendMeetings(intervals [][]int) bool {
	if len(intervals) <= 1 {
		return true
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] < intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})
	for i := 0; i < len(intervals)-1; i++ {
		if intervals[i][1] > intervals[i+1][0] {
			return false
		}
	}
	return true
}
