/*
 * time: O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges).
 * space: O(V + E), where V is for the map and sets and E is for call stacks, which is bounded by the number of courses and prerequisites.
 */
class Solution {

    Map<Integer, List<Integer>> courseToPrerequisites = new HashMap<>();
    Set<Integer> traversing = new HashSet<>();
    Set<Integer> finished = new HashSet<>();

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for (int[] prerequisite : prerequisites) {
            courseToPrerequisites.computeIfAbsent(prerequisite[0], key -> new ArrayList<>())
                                 .add(prerequisite[1]);
        }

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(int course) {
        if (traversing.contains(course)) {
            return false;
        }
        if (finished.contains(course)) {
            return true;
        }

        traversing.add(course);
        if (courseToPrerequisites.containsKey(course)) {
            List<Integer> requisites = courseToPrerequisites.get(course);
            for (int req : requisites) {
                if (!dfs(req)) {
                    return false;
                }
            }
        }
        traversing.remove(course);
        finished.add(course);
        return true;
    }
}
