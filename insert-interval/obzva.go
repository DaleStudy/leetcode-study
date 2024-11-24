/*
풀이
- newInterval의 start와 end에 대해 각각 이진탐색을 진행하여 insert할 index를 찾아낼 수 있습니다
- index의 앞뒤 interval과 newInterval을 비교하여 merge 여부를 판별하면 문제에서 원하는 배열을 만들 수 있습니다
Big O
- N: 주어진 배열 intervals의 길이
- Time complexity: O(N)
  - 이진 탐색 -> O(logN)
  - append(res, ...) -> O(N)
  - O(N + logN) = O(N)
- Space complexity: O(N)
  - 반환하는 배열 res의 공간 복잡도를 고려하면 O(N)
*/

func insert(intervals [][]int, newInterval []int) [][]int {
	n := len(intervals)
	// base case
	if n == 0 {
		return append(intervals, newInterval)
	}
	// 이진탐색 함수
	// isStart: newInterval의 start를 탐색할 땐 true, end를 탐색할 땐 false
	// target보다 큰 값 중에서 가장 작은 index를 반환함
	var binarySearch func(int, bool) int
	binarySearch = func(target int, isStart bool) int {
		lo := 0
		hi := len(intervals)
		for lo < hi {
			mid := lo + (hi-lo)/2
			if isStart {
				if intervals[mid][0] < target {
					lo = mid + 1
				} else {
					hi = mid
				}
			} else {
				if intervals[mid][1] < target {
					lo = mid + 1
				} else {
					hi = mid
				}
			}
		}
		return lo
	}

	start := binarySearch(newInterval[0], true)
	// newInterval의 시작 지점이 intervals[start-1]의 끝 지점보다 작거나 같으면 merge해야 함
	mergeStart := start > 0 && newInterval[0] <= intervals[start-1][1]
	end := binarySearch(newInterval[1], false) - 1
	// newInterval의 끝 지점이 intervals[end+1]의 시작 지점보다 크거나 같으면 merge해야 함
	mergeEnd := end+1 < n && newInterval[1] >= intervals[end+1][0]

	// -Go에서의 최적화를 위한 코드입니다-
	resCapacity := n + 1
	if mergeStart {
		resCapacity--
	}
	if mergeEnd {
		resCapacity--
	}
	// -----------------------------
	res := make([][]int, 0, resCapacity)
	// newInterval이 들어갈 index보다 앞 부분의 값들을 res에 append
	if mergeStart {
		res = append(res, intervals[:start-1]...)
	} else {
		res = append(res, intervals[:start]...)
	}
	// newInterval을 res에 append
	// mergeStart, mergeEnd 여부에 따라 병합할지 그대로 넣을지 판단
	if mergeStart && mergeEnd {
		res = append(res, []int{intervals[start-1][0], intervals[end+1][1]})
	} else if mergeStart {
		res = append(res, []int{intervals[start-1][0], newInterval[1]})
	} else if mergeEnd {
		res = append(res, []int{newInterval[0], intervals[end+1][1]})
	} else {
		res = append(res, newInterval)
	}
	// newInterval이 들어갈 index보다 뒷 부분의 값들을 res에 append
	if mergeEnd {
		res = append(res, intervals[end+2:]...)
	} else {
		res = append(res, intervals[end+1:]...)
	}

	return res
}
