/*
풀이
- 나머지 interval이 overlapping하지 않도록 하기 위해 제거해야 하는 interval의 최소 개수 구하기 문제
  = 서로 overlapping하지 않도록 interval을 담은 배열의 최대 길이 구하기 문제
- Activity Selection Problem이라는 유형의 문제로 치환할 수 있음 (https://en.wikipedia.org/wiki/Activity_selection_problem)
- 이 문제의 그리디 증명은 블로그에 정리해두었음 (https://blog.naver.com/sigmapi1000/223532427648?trackingCode=blog_bloghome_searchlist)
Big O
- N: intervals의 길이
- Time complexity: O(NlogN)
  - sort.Slice -> O(NlogN)
  - 두 번째 for문 -> O(N)
- Space complexity: O(logN)
  - sort.Slice는 퀵소트의 일종을 사용하므로 재귀 호출 스택의 깊이를 고려하여야 함
*/

import "sort"

func eraseOverlapIntervals(intervals [][]int) int {
	n := len(intervals)
	if n == 1 {
		return 0
	}
	sort.Slice(intervals, func(i, j int) bool { // end의 오름차순으로 정렬
		return intervals[i][1] < intervals[j][1]
	})
	res := 0
	prev := 0 // 이전 interval을 가리킴
	curr := 1 // 현재 interval을 가리킴
	for curr < len(intervals) {
		if intervals[prev][1] > intervals[curr][0] {
			res++
			curr++
		} else {
			prev = curr
			curr++
		}
	}
	return res
}