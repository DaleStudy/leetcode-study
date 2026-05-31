class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> ans;
        int n = intervals.size();
        int i = 0;

        while (i < n && intervals[i][1] < newInterval[0]) {
            ans.push_back(intervals[i]);
            i++;
        }

        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        ans.push_back(newInterval);

        while (i < n) {
            ans.push_back(intervals[i]);
            i++;
        }
        
        return ans;
    }

    // vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    //     vector<vector<int>> ans;
    //     bool tmp = false;
    //     int left = newInterval[0], right = newInterval[1];
        
    //         for(int i = 0; i < intervals.size(); i++) {
    //         if(intervals[i][1] < left) {
    //             ans.push_back(intervals[i]);
    //             continue;
    //         }
    //         else if(right < intervals[i][0]) {
    //             if(!tmp) {
    //                 ans.push_back(vector<int>({left, right}));
    //                 tmp = true;
    //             }
    //             ans.push_back(intervals[i]);
    //             continue;
    //         }
    //         else {
    //             left = min(left, intervals[i][0]);
    //             right = max(right, intervals[i][1]);
    //         }
    //     }

    //     if(!tmp)
    //         ans.push_back(vector<int>({left, right}));

    //     return ans;   
    // }
};

