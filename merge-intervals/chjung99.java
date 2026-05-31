class Solution {
    public int[][] merge(int[][] intervals) {
        //sort by start_i
        List<Interval> ordered = new ArrayList<>();
        for (int i = 0; i < intervals.length; i++){
            ordered.add(new Interval(intervals[i]));
        }
        Collections.sort(ordered);

        Deque<Interval> queue = new ArrayDeque<>();
        queue.add(ordered.get(0));
        //merge in order
        for (int i = 1; i < ordered.size(); i++) {
            Interval tail = queue.removeLast();
            Interval cur = ordered.get(i);

            if (tail.end >= cur.start){
                Interval merged = new Interval(new int[]{Math.min(tail.start, cur.start), Math.max(tail.end, cur.end)});
                queue.add(merged);
            } else{
                queue.add(tail);
                queue.add(cur);
            }
        }
        int[][] answer = new int[queue.size()][2];
        int idx = 0;
        while (!queue.isEmpty()){
            answer[idx++] = queue.removeFirst().raw;
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


