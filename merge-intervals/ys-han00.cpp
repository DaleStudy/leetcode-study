class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
    
        vector<vector<int>> ans;        
        for (const auto& interval : intervals) {
            if (ans.empty() || ans.back()[1] < interval[0])
                ans.push_back(interval);
            else
                ans.back()[1] = max(ans.back()[1], interval[1]);
        }
        
        return ans;
    }

    // vector<vector<int>> merge(vector<vector<int>>& intervals) {
    //     vector<vector<int>> ans;
    //     sort(intervals.begin(), intervals.end());
        
    //     int idx = 0, s, e;
    //     s = intervals[idx][0];
    //     e = intervals[idx][1];
    //     idx++;
    //     while(idx < intervals.size()) {
    //         if(e < intervals[idx][0]) {
    //             ans.push_back(vector<int>({s, e}));
    //             s = intervals[idx][0];
    //             e = intervals[idx][1];
    //         } else {
    //             e = max(e, intervals[idx][1]);
    //         }
    //         idx++;
    //     }
    //     ans.push_back(vector<int>({s, e}));

    //     return ans;
    // }
};

