// 풀이
// 1 일 때, 가능한 step은 1 -> 1가지
// 2 일 때, 가능한 step은 1 1, 2 -> 2가지
// 3 일 때, 가능한 step은 1 1 1, 1 2, 2 1 -> 3가지
// n 일 때, 가능한 stop은 n-1의 가짓수에 1이 붙고, n-2의 가짓수에 2가 붙는다.

// TC
// O(n)

// SC
// int타입 변수만 사용해서 O(1)

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	prev := 1 // climb1
	curr := 2 // climb2
	for i := 3; i <= n; i++ {
		prev, curr = curr, (curr + prev)
	}
	return curr
}
