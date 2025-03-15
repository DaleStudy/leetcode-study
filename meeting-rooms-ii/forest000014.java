/*
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
*/

class Solution {

    private class Info {
        int kind; // start = 0, end = 1
        int time;

        Info(int kind, int time) {
            this.kind = kind;
            this.time = time;
        }
    }
    public int minMeetingRooms(int[][] intervals) {
        int n = intervals.length;
        List<Info> infos = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            infos.add(new Info(0, intervals[i][0]));
            infos.add(new Info(1, intervals[i][1]));
        }

        Collections.sort(infos, (o1, o2) -> {
            if (o1.time == o2.time) {
                return Integer.compare(o2.kind, o1.kind);
            }
            return Integer.compare(o1.time, o2.time);
        });

        int cnt = 0;
        int ans = 0;
        for (Info info : infos) {
            if (info.kind == 0) cnt++;
            else cnt--;
            ans = Math.max(ans, cnt);
        }

        return ans;
    }
}
