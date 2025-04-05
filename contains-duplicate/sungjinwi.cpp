/*
    set를 통해 중복제거를 한 후 기존 nums와 길이 비교

    nums의 길이 N

    TC : O(N)
        set를 만드는 데 전체 순회하며 N 시간 소모

    SC : O(N)
        set 만들 때 N의 메모리 할당
*/
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> us(nums.begin(), nums.end());
        if (nums.size() == us.size())
            return false;
        else
            return true;
    }
};
