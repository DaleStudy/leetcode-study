class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        int ans = 0;
        int k = INT_MIN;
        
        for (int i = 0; i < intervals.size(); i++) 
        {
            int s = intervals[i][0];
            int e = intervals[i][1];
            
            if (s >= k) 
            {
                k = e;
            } 
            else 
            {
                ans++;
            }
        }
        
        return ans;
    }
};
