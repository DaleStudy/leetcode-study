/*
    풀이 :
        현재 집의 순서를 n이라고 했을 때 값을 업데이트하기 전 cur에는 n - 1 집까지 최대 훔칠 수 있는 돈, prv에는 n - 2집까지 최대 훔칠 수 있는 돈이 저장
        cur를 max(n - 2까지 돈 + n의 돈, n - 1까지의 돈)로 n까지 오면서 훔칠 수 있는 최대 돈으로 업데이트,
        prv는 n - 1까지 훔칠 수 있는 최대 돈으로 업데이트
    
    nums의 갯수 : N

    TC : O(N)

    SC : O(1)
        배열없이 상수 변수 3개만 추가로 사용
*/

#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int prv = 0, cur = 0;
        int tmp;
        for (auto& num : nums)
        {
            tmp = cur;
            cur = max(prv + num, cur);
            prv = tmp;
        }
        return cur;
    }
};
