# Intuition
It is a simple `greedy` problem.
간단한 그리디 분류의 문제다. 
# Approach 
1. To find earliest interval, sort intervals by start time in ascending order.
2. After sorting, while iterating through the array, check for conflict: the current interval's start time shoud be smaller than the next interval's end time.
# Complexity
- Time complexity: $$O(nlog(n))$$
- Space complexity: $$O(n)$$

(n is length of `intervals`)
# Code
```go
func CanAttendMeetings(intervals []*Interval) bool {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})

	curr := &Interval{-1, -1}
	for _, next := range intervals {
		if curr.End > next.Start {
			return false
		}
		curr = next
	}

	return true
}
```