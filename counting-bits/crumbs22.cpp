/*
    n + 1번 반복하며 dp배열에 저장하기 때문에 시간복잡도 O(n), 공간복잡도 O(n)만큼 소요
*/
class Solution {
	public:
		vector<int> countBits(int n) {
			vector<int> dp(n + 1, 0); // 0부터 n까지이므로 n + 1개 필요, dp[0] = 0
	
			// dp배열을 활용, 최상위비트 + (마지막비트&1)를 dp에 저장
			for (int num = 1; num < n + 1; num++) {
				dp[num] = dp[num >> 1] + (num & 1);
			}
			return dp;
		}
	};
