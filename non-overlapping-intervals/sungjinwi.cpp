class Solution {
    public:
        int eraseOverlapIntervals(vector<vector<int>>& intervals) {

            sort(intervals.begin(), intervals.end(), [] (vector<int>& a, vector<int>& b){ return a[1] < b[1]; });
    
            int cnt = 0;
            int lastEnd = INT_MIN;

            for (auto& interval : intervals) {
                if (interval[0] < lastEnd)
                    cnt++;
                else
                    lastEnd = interval[1];
            }

            return cnt;
        }
    };
