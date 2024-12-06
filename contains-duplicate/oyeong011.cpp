#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(int a : nums){
            if(++mp[a] >= 2){
                return true;
            }
        }
        return false;
    }
};