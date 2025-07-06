class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        if(intervals.empty())
            return 0;
        
        vector<int> starts, ends;

        for(int i = 0; i < intervals.size(); i++){
            starts.push_back(intervals[i].start);
            ends.push_back(intervals[i].end);
        }

        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        int result = 0;
        int endpos = 0;

        for(int i = 0; i < starts.size(); i++){
            if(starts[i] < ends[endpos])
                result++;
            else
                endpos++;
        }

        return result;
    }
};
