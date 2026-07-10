// 문제 풀이 흐름
// 누가봐도 점화식 -> DP 문제이다.
// 자세히 보니 피보나치수열 같음
// 1,2번쨰 항일때만 주의해서 풀자.

// n에 대해서
// 시간복잡도 : O(n)
// 공간복잡도 : O(1)

class Solution {
	public int climbStairs(int n) {
		if (n == 1) return 1;
		if (n == 2) return 2;

		// 3 = 2 * [1] + [2]
		// 4 = 2 * [2] + [3]
		int doublePrev = 0;
		int prev = 1;
		int current = 2;

		for (int i = 3 ; i <= n ; i++ ) {
			doublePrev = prev;
			prev = current;
			current = doublePrev + prev;
		}
		return current;
	}
}
