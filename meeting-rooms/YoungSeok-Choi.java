import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Interval {
    int start, end;

    Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

class Solution {

    public boolean canAttendMeetings(List<Interval> intervals) {
        Collections.sort(intervals, new Comparator<Interval>() {
            @Override
            public int compare(Interval i1, Interval i2) {
                if (i1.start == i2.start) {
                    return i1.end - i2.end;
                }

                return i1.start - i2.start;
            }
        });

        int prevEnd = -987654321;
        for (Interval anInt : intervals) {
            if (anInt.start < prevEnd) {
                return false;
            }

            prevEnd = anInt.end;
        }

        return true;
    }
}
