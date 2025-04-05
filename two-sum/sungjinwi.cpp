/*
    풀이 :
        타깃을 뺸 complement 값을 구하고 해시테이블(unordered_map)에 존재하면 리턴
        없으면 해시테이블에 값 : 인덱스 형태로 저장

    nums의 size: N
    TC : O(N)
        size만큼 for문 반복
    SC : O(N)
        size만큼 해시테이블에 추가
*/

#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if (umap.find(complement) == umap.end())
                umap[nums[i]] = i;
            else
            {
                result.push_back(i);
                result.push_back(umap[complement]);
                return result;
            }
        }
        return result;
    }
};
