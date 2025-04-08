/*
    풀이 :
        해시테이블에 nums를 담은 뒤 num - 1이 존재하지 않는 num에 대해서만 (중간점에서는 계산하지 않기 위해)
        길이를 증가시켜 나가며 연속된 수의 개수를 구하고 cur의 max값 ans를 구한다

    nums의 갯수 N
    TC : O(N)
        이중 for문이지만 내부 for문은 num - 1이 없을때만 연속된 해시테이블 내부 값에 대해서 수행하기 때문에 O(N)
    
    SC : O(N)
        해시테이블의 크기는 N에 비례
*/

#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int cur;
        int ans = 0;
        unordered_set<int> us(nums.begin(), nums.end());

        for (auto& num : us)
        {
            if (us.find(num - 1) == us.end())
            {
                cur = 1;
                for(int i = 1; us.find(num + i) != us.end(); i++)
                    cur++;
                ans = max(ans, cur);
            }
        }
        return ans;
    }
};
