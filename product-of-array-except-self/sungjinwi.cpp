/*
    풀이 :
        해당 인덱스 이전 값들의 곱을 before에 저장(인덱스 0 이전에는 값이 없으므로 1로 초기화)
        해당 인덱스 이후 값들의 곱을 after에 저장(인덱스 n - 1이후에는 값이 없으므로 1로 초기화)
        인덱스 0부터 반복문을 돌며 ans에 인덱스 이전값들의 곱 before를 곱함 & before값에 현재 num을 곱함
        인덱스 끝부터 반복문을 돌며 after를 이용해 동일 작업

    nums의 길이 : N

    TC : O(N)
        반복문 2회 O(N + N)
    
    SC : O(1) (ans배열 제외)
        N에 관계없이 before와 after 변수만 사용
*/

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int before = 1;
        int after = 1;
        vector<int> ans(nums.size(), 1);

        for (int i = 0; i < nums.size(); i++)
        {
            ans[i] *= before;
            before *= nums[i];
        }
        for (int i = nums.size() - 1; i >= 0; i--)
        {
            ans[i] *= after;
            after *= nums[i];
        }
        return ans;
    }
};
