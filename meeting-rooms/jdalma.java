package leetcode;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class jdalma {

    public class Interval {
        public int start, end;

        public Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    public boolean canAttendMeetings(List<Interval> intervals) {
        return usingBruteForce(intervals);
    }

    /**
     * TC: O(n^2), SC: O(1)
     */
    private boolean usingBruteForce(List<Interval> intervals) {
        final int size = intervals.size();
        for (int i = 0; i < size; i++) {
            Interval A = intervals.get(i);
            for (int j = i + 1; j < size; j++) {
                Interval B = intervals.get(j);
                if (Math.min(A.end, B.end) > Math.max(A.start, B.start)) {
                    return false;
                }
            }
        }
        return true;
    }

    /**
     * TC: O(n log n), SC: O(1)
     */
    private boolean usingSort(List<Interval> intervals) {
        intervals.sort(Comparator.comparingInt(i -> i.start));

        for (int i = 1; i < intervals.size(); i++) {
            Interval first = intervals.get(i - 1);
            Interval second = intervals.get(i);

            if (first.end > second.start) {
                return false;
            }
        }

        return true;
    }

    @Test
    @DisplayName("입력받은 간격들의 충돌 여부를 반환한다.")
    void name() {
        Assertions.assertThat(canAttendMeetings(new ArrayList<>() {
            {
                add(new Interval(0, 30));
                add(new Interval(5, 10));
                add(new Interval(15, 20));
            }
        })).isFalse();

        Assertions.assertThat(canAttendMeetings(new ArrayList<>() {
            {
                add(new Interval(5, 8));
                add(new Interval(9, 10));
            }
        })).isTrue();
    }
}
