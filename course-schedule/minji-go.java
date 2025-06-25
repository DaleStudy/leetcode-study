/**
 * <a href="https://leetcode.com/problems/course-schedule/">week10-3. course-schedule   </a>
 * <li>Description: Return true if you can finish all courses. Otherwise, return false  </li>
 * <li>Topics: Depth-First Search, Breadth-First Search, Graph, Topological Sort        </li>
 * <li>Time Complexity: O(N+E), Runtime 7ms        </li>
 * <li>Space Complexity: O(N+E), Memory 45.68MB    </li>
 * <li>Note : refer to the answer. remember the topic of topological sort </li>
 */
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        List<List<Integer>> graph = new ArrayList<>();
        for (int i=0; i<numCourses; i++){
            graph.add(new ArrayList<>());
        }

        for(int[] pre : prerequisites) {
            int dest = pre[0], src = pre[1];
            graph.get(src).add(dest);
            inDegree[dest]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i=0; i<numCourses; i++) {
            if(inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        int count = 0;
        while(!queue.isEmpty()){
            int node = queue.poll();
            count++;

            for(int neighbor : graph.get(node)) {
                inDegree[neighbor]--;
                if(inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        return count == numCourses;
    }
}
