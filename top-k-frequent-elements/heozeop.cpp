// Time complexity O(nlogn)
// Spatal Complexity O(n)

#include <map>
#include <vector>

using namespace std;


bool cmp(const pair<int,int>& a, const pair<int,int>& b) {
    return a.second > b.second;
}

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> countMap;

        for(int num : nums) {
            if(countMap.find(num) == countMap.end()) {
                countMap.insert({num, 0});
            }
            
            ++countMap[num];
        }

        vector<pair<int,int>> vec(countMap.begin(), countMap.end());
        sort(vec.begin(), vec.end(), cmp);

        vector<int> answer;
        for(int i = 0; i < k; ++i) {
            answer.push_back(vec[i].first);
        }

        return answer;
    }
};

