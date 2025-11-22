#include <bits/stdc++.h>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < nums.size() - 1; i++)
            if(nums[i] == nums[i+1])
                return true;

        return false;
    }
};

// 첫 시도 및 틀린 풀이
// 틀린 이유:
//   leetcode는 처음 풀어보는데, 백준보다 시간 제한이 엄격함
//   -> 20억 배열 선언하는것만으로도 시간초과 발생
// 
// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
//         vector<bool> check(2'000'000'001, false);
//         int offset = 1'000'000'000;

//         for(int i = 0; i < nums.size(); i++) {
//             int idx = nums[i] + offset;
            
//             if(check[idx] == true)
//                 return true;
//             check[idx] = true;
//         }
//         return false;
//     }
// };

