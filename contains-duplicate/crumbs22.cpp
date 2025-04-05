#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
		unordered_set<int> uset(nums.begin(), nums.end());
		return (nums.size() != uset.size());
    }
};
