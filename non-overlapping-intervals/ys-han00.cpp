class Solution {
public:
    static bool comp(const vector<int> &a, const vector<int> &b) {
        return (a[1] == b[1] ? a[0] > b[0] : a[1] < b[1]);
    }
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), comp);
        int ans = 0, prev_end = intervals[0][1], start, end;
        for(int i = 1; i < intervals.size(); i++) {
            if(prev_end > intervals[i][0]) 
                ans++;
            else
                prev_end = intervals[i][1];
        }

        return ans;
    }
};

