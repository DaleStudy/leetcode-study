/*
    풀이 : 
        해시테이블에 숫자 : 빈도로 저장 후 freq 이중배열에 index를 frequency로 삼아 저장한다
        이중배열의 뒤에서부터 탐색하면서 k개를 result에 삽입

    nums 개수 N
    TC : O(N)
        전체 개수 N에 대해 for문 각각 돌아서
    SC : O(N)
        해시테이블과 이중배열 모두 N에 비례
*/

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> umap;
        for (auto& num : nums)
        {
            umap[num]++;
        }

        vector<vector<int>> freq(nums.size() + 1);
        for (auto& pair : umap)
        {
            freq[pair.second].push_back(pair.first);
        }
        
        vector<int> result;
        for (int i = nums.size(); i > 0 && result.size() < k; i--)
        {
            for (auto& num : freq[i])
            {
                result.push_back(num);
                if (result.size() == k)
                    break ;
            }
        }
        return result;
    }
};
