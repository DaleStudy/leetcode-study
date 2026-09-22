import java.util.ArrayList;
import java.util.List;

// TC: O(V + E)
// SC: O(V + E)
class Solution {
    private static final int UNVISITED = 0;
    private static final int VISITING = 1;
    private static final int VISITED = 2;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> nextCourses = new ArrayList<>(numCourses);
        int[] visitState = new int[numCourses];

        for (int course = 0; course < numCourses; course++) {
            nextCourses.add(new ArrayList<>());
        }

        for (int[] dependency : prerequisites) {
            int course = dependency[0];
            int prerequisite = dependency[1];
            nextCourses.get(prerequisite).add(course);
        }

        for (int course = 0; course < numCourses; course++) {
            if (visitState[course] == UNVISITED
                    && hasCycle(course, nextCourses, visitState)) {
                return false;
            }
        }

        return true;
    }

    private boolean hasCycle(
            int course,
            List<List<Integer>> nextCourses,
            int[] visitState
    ) {
        if (visitState[course] == VISITING) {
            return true;
        }
        if (visitState[course] == VISITED) {
            return false;
        }

        visitState[course] = VISITING;

        for (int nextCourse : nextCourses.get(course)) {
            if (hasCycle(nextCourse, nextCourses, visitState)) {
                return true;
            }
        }

        visitState[course] = VISITED;
        return false;
    }
}
