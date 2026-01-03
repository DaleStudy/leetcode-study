class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        Deque<Interval> deque = new ArrayDeque<>();
        List<Interval> ordered = new ArrayList<>();
        List<Interval> merged = new ArrayList<>();

        for (int i = 0; i < intervals.length; i++){
            ordered.add(new Interval(intervals[i]));
        }

        ordered.add(new Interval(newInterval));
        Collections.sort(ordered);

        Interval cur;
        Interval next;

        int curIdx = 0;
        deque.add(ordered.get(0));

        while (curIdx < ordered.size()){
            cur = deque.removeLast();

            if (curIdx + 1 < ordered.size()){
                next = ordered.get(curIdx + 1);
                if (next.start <= cur.end){ // merge
                    Interval mergedInterval = new Interval( new int[]{
                            Math.min(cur.start, next.start), Math.max(cur.end, next.end)
                    });
                    deque.addLast(mergedInterval);
                } else {
                    deque.addLast(cur);
                    deque.addLast(next);
                }

            } else {
                deque.addLast(cur);
            }
            curIdx ++;
        }
        int[][] answer = new int[deque.size()][2];
        int idx = 0;
        while (!deque.isEmpty()){
            answer[idx++] = deque.removeFirst().raw;
        }
        return answer;
    }
    class Interval implements Comparable<Interval>{
        int[] raw;
        int start;
        int end;

        public Interval(int[] raw){
            this.raw = raw;
            this.start = raw[0];
            this.end = raw[1];
        }

        @Override
        public int compareTo(Interval o){
            return Integer.compare(this.start, o.start);
        }
    }
}


