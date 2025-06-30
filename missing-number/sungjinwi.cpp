/*
    풀이 : 
        수식을 이용해 숫자가 빠지지 않았을경우 총합을 구하고 nums를 순회하면서 숫자들을 빼면 남은 숫자가 missing No.

    nums의 길이 : N

    TC : O(N)
    
    SC : O(1)
*/

#include <vector>
using namespace std;

class Solution {
    public:
        int missingNumber(vector<int>& nums) {
            int n = nums.size();
            int sum = n * (n + 1) / 2;
    
            for (auto& num : nums)
                sum -= num;
            return sum;
        }
    };
