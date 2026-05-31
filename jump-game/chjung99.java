class Solution {
    boolean isArrived;
    int SIZE;

    public boolean canJump(int[] nums) {
        isArrived = false;
        SIZE = nums.length;

        bfs(nums, 0);

        return isArrived;
    }

    public void bfs(int[] nums, int x) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(x);
        boolean[] visit = new boolean[SIZE];
        visit[x] = true;

        int curX;
        int nextX;

        while (!q.isEmpty()){
            curX = q.poll();
            isArrived = (curX + 1) == SIZE;
            if (isArrived) return;

            for (int dx = 1; dx <= nums[curX]; dx++){
                nextX = curX + dx;
                if (nextX >= SIZE || visit[nextX]) continue;
                q.add(nextX);
                visit[nextX] = true;
            }
        }
    }
}


