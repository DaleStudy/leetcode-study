/*
    풀이 :
        max_sum은 INT_MIN으로 초기화

        수를 순회하면서 sum에 num을 더한다(subarray의 합)
        max_sum과 현재 subarray합을 비교해 업데이트한다

        subarray의 합이 0보다 작으면 새로운 subarray를 시작하기 위해 sum을 0으로 초기화한다

    nums의 길이 N

    TC : O(N)

    SC : O(1)
*/

#include <vector>
#include <limits.h>
using namespace std;

class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int max_sum = INT_MIN;
            int sum = 0;
    
            for (auto& num : nums)
            {
                sum += num;
                if (max_sum < sum)
                    max_sum = sum;
                if (sum < 0)
                    sum = 0;
            }
            return max_sum;
        }
    };
