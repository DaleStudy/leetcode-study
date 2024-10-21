// TC: O(n + p)
// n -> number of courses, p -> the length of prerequisites
// SC: O(n + m)
// n -> the length of the graph size, m -> the length of nested list's size
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());

        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int pre = prerequisite[1];
            graph.get(pre).add(course);
            inDegree[course] += 1;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) q.offer(i);
        }

        int visitedCourses = 0;
        while (!q.isEmpty()) {
            int course = q.poll();
            visitedCourses += 1;

            for (int nextCourse : graph.get(course)) {
                inDegree[nextCourse] -= 1;
                if (inDegree[nextCourse] == 0) q.offer(nextCourse);
            }
        }

        return visitedCourses == numCourses;
    }
}
