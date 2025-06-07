public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] degree = new int[numCourses];

        Map<Integer, List<Integer>> graph = new HashMap<>();

        for (int[] p : prerequisites) {
            int course = p[0];
            int pre = p[1];

            degree[course]++;

            if (!graph.containsKey(pre)) {
                graph.put(pre, new ArrayList<>());
            }
            graph.get(pre).add(course);
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (degree[i] == 0) {
                q.offer(i);
            }
        }

        int finishedCourses = 0;

        while (!q.isEmpty()) {
            int curr = q.poll();
            finishedCourses++;

            if (graph.containsKey(curr)) {
                for (int neighbor : graph.get(curr)) {
                    degree[neighbor]--;
                    if (degree[neighbor] == 0) {
                        q.offer(neighbor);
                    }
                }
            }
        }

        if(finishedCourses == numCourses) return true;

        return false;
    }
}

