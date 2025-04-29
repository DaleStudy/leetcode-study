#include <vector>
#include <algorithm>
using namespace std;

/*
	- dp[i]: 금액 i를 만드는 최소 코인수
	- 초기값
		- dp[0] = 0
		- 그 외에는 amount + 1 (도달할 수 없는 값)으로 초기화
	- 현재 금액 i를 만들기 위해서
		이전 금액인 i - c를 만들고, 거기에 코인 c를 더 썼을 때 최소값을 갱신함
	예시) coins = [1, 2, 5], i = 3일 때
			c = 1 ->  3 >= 1 이므로 dp[3] = min(dp[3], dp[2] + 1) 갱신
			c = 2 ->  3 >= 2 이므로 dp[3] = min(dp[3], dp[1] + 1) 갱신
			c = 5 ->  3 < 5 이므로 건너뜀
		=> i - c가 음수면 배열 범위를 벗어나므로 i >= c일때만 연산산
*/
class Solution {
public:
	int coinChange(vector<int>& coins, int amount) {
		// dp 테이블 초기화
		vector<int> dp(amount + 1, amount + 1);
		dp[0] = 0;

		// bottom up 연산
		for (int i = 1; i <= amount; ++i) {
			for (int c : coins) {
				if (i >= c) {
					dp[i] = min(dp[i], dp[i - c] + 1);
				}
			}
		}

		return (dp[amount] > amount) ? -1 : dp[amount];
	}
};
