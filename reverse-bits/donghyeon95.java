public class Solution {
	// you need treat n as an unsigned value
	public int reverseBits(int n) {
		int result = 0;

		for (int i = 0; i < 32; i++) {
			// 왼쪽으로 비트를 한 칸 이동하고, n의 마지막 비트를 추가
			result = (result << 1) | (n & 1);
			// n을 오른쪽으로 한 칸 이동
			n >>= 1;
		}

		return result;
	}
}

