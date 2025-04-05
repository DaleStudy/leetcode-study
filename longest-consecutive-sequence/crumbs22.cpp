#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        int cnt = 0;
        int max = 0;

        int i = *s.begin();
        for (set<int>::iterator iter = s.begin(); iter != s.end(); iter++)
        {
            cout << *iter << endl;
            if (*iter != i)
            {
                cnt = 1;
                i = *iter + 1;
                continue;
            }
            cnt++;
            i++;
            if (cnt > max)
                max = cnt;
        }
        return (max);
    }
};
