
// TC: O(N)
// SC: O(1)
class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    public boolean canAttendMeetings(List<Interval> intervals) {
        // Edge case: empty list or single meeting
        if (intervals == null || intervals.size() <= 1) {
            return true;
        }
        
        intervals.sort(Comparator.comparing(v->v.start));
        
        int prevEndTime = intervals.get(0).end;
        for(int i = 1; i < intervals.size(); i++){  
            Interval cur = intervals.get(i);
            if(cur.start < prevEndTime) return false;
            prevEndTime = cur.end;
        }
        return true;
    }
}

