// 문제풀이 흐름
// 어떤 숫자를 2진수로 나타냈을때, 1의 개수를 구하는 것이므로
// 2진수 변환과정에서 나오는 모든 1의 갯수만 세면 된다.

// 숫자 n에 대하여
// 시간복잡도 : O(logn)
// 공간복잡도 : O(1)

class Solution {
	public int hammingWeight(int n) {
		int answer = 0;

		while (n > 0) {
			if (n % 2 == 1) answer ++;
			n /= 2;
		}

		return answer;
	}
}
