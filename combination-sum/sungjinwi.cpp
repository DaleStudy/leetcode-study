/*
    풀이 :
        target + 1개의 크기를 가지는 삼중벡터 dp를 만든다
        dp[n] = dp[n - candidate]의 각 조합에 candidate를 추가하는 로직으로 쌓아나갈 것이다
            dp[n - c]가 [comb1, comb2]일 때 dp[n]은 [comb1.push_back(c), comb2.push_back[2]]

        dp[0]은 연산을 위해 빈 이중 벡터로 초기화 ( dp[n] = dp[n - n] = dp[0] --> [[].push_back(n)])

    target크기 : T, candidate 갯수 : N

    TC : O(T * N)

    SC : O(T * N)
*/

#include <vector>
using namespace std;

class Solution {
    public:
        vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
            vector<vector<vector<int>>> dp(target + 1);
            dp[0] = {{}};
            for (int candidate : candidates)
            {
                for (int num = candidate; num <= target; num++)
                {
                    for (auto& combination : dp[num - candidate])
                    {
                        vector<int> new_comb = combination;
                        new_comb.push_back(candidate);
                        dp[num].push_back(new_comb);
                    }
                }
            }
            return dp[target];
        }
    };
