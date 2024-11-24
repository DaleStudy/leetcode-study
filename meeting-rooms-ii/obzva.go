/*
풀이
- 회의의 시작시간과 종료시간을 각각 오름차순 정렬하여 풀이할 수 있습니다
Big O
- N: 주어진 배열 intervals의 길이
- Time complexity: O(NlogN)
  - starts, ends 생성 -> O(N)
  - slices.Sort() -> O(NlogN)
  - 마지막 반복문 -> O(N)
- Space complexity: O(logN)
  - Go의 slices.Sort()는 퀵소트를 이용하므로 재귀 호출 스택 깊이 O(logN)이 고려되어야 함
*/

import "slices"

func minMeetingRooms(intervals [][]int) int {
	n := len(intervals)

	if n == 1 {
		return 1
	}

	starts := make([]int, n) // 회의 시작시간들
	ends := make([]int, n)   // 회의 종료시간들
	for i, interval := range intervals {
		starts[i] = interval[0]
		ends[i] = interval[1]
	}
	// 오름차순 정렬
	slices.Sort(starts)
	slices.Sort(ends)

	rooms := 0
	sPtr := 0
	ePtr := 0
	for sPtr < n {
		if starts[sPtr] < ends[ePtr] { // 현재 사용가능한 회의실이 없음 (현재 진행중인 모든 회의가 starts[sPtr]보다 큼)
			rooms++ // 새로운 회의실 추가함
		} else {
			ePtr++ // 기존 회의실 중에 남는 방이 있음, 새로운 회의실 추가하지 않음
		}
		sPtr++
	}

	return rooms
}
