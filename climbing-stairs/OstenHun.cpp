/*
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?

    Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Constraints:
    1 <= n <= 45
*/

// TimeComplexity : O(n)
// SpaceComplexity : O(n)
#include <iostream>
using namespace std;

#pragma region DpArrayIdea
namespace dp_array_idea {

class Solution {
public:
    int climbStairs(int n) {
        int dp[45];

        // dp[i]는 i-1번째 칸을 오르는 경우의 수를 말한다.
        dp[0] = 1;
        dp[1] = 2;

        for (int i = 2; i < n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n-1];
    }
};

}  // namespace dp_array_idea
#pragma endregion

// 배열을 사용하지 않는 풀이
// Time : O(n)
// Space : O(1)
#pragma region FinalSolution
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int one_back = 1;
        int two_back = 2;

        for (int i = 3; i <= n; i++) {
            int current = one_back + two_back;
            two_back = one_back;
            one_back = current;
        }

        return one_back;
    }
};
#pragma endregion
