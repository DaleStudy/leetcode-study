
/*
* 처음 풀이
* n개 중 2를 선택하는 조합 문제로 해결
* 21부터 overflow 발생 => 너무 큰 숫자
* 이대로 푸려면 1과 2의 갯수가 정확하게 같아지는 경우 * 2를 하면 f(1갯수, 2갯수) 할 때, f(x, y) = f(y,x)는 같다는 점을 착안하면 42까지는 풀 수 있을 듯 하다.
* 하지만 45라서 안되는 거 같다.
* */

// public int climbStairs(int n) {
// 	// N개의 1중에서 묶이는 경우의 수가 몇개인지
// 	// 5 => 1 1 1 1 1
// 	// 2의 갯수가 0개 2/n 까지 있는 경우의 수를 구하면 될 듯
// 	long result = 0;
// 	int max2Cnt = n/2;
// 	for (int i=0; i<max2Cnt+1; i++) {
// 		int cnt = n-2*i + i; // 조합을 구해야 하는 숫자의 갯수는 2의 개수 + 1의 갯수
// 		result += factorial(cnt) / (factorial(i) * factorial(cnt-i));
// 	}
//
// 	for (long k: nFact) {
// 		System.out.println(k);
// 	}
//
// 	return (int)result;
// }
//
// public long factorial(int i) {
// 	if (nFact[i] != 0) return nFact[i];
// 	if (i == 0 || i == 1) {
// 		nFact[i] = 1;
// 		return 1;
// 	}
//
// 	long result = i * factorial(i - 1);
// 	nFact[i] = result;
// 	return result;
// }

/*
* 두번째 풀이
* 나의 계단을 오르는 경우 = 이전에 1칸 오른 경우의 수 + 이전에 2칸 오른 경우의 수
* 시간 복잡도 O(N)에 해결 가능하다.
* */

class Solution {
	public int climbStairs(int n) {
		// k번째의 계단을 오르는 경우의 수는
		// k-1 번째 계단을 오르는 경우의 수 + K-2번째 계단을 오르는 경우의 수
		if (n <= 2) return n;

		int first = 1;
		int second = 2;

		for (int i = 3; i <= n; i++) {
			int third = first + second;
			first = second;
			second = third;
		}

		return second;
	}
}

