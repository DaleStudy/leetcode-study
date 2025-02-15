class Solution {
	public int hammingWeight(int n) {
		int mask = 1;
		int result = 0;
		while(n>0) {
			if ((n & mask) == 1) {
				result++;
			}
			n = n >> 1;
		}

		return result;
	}
}

