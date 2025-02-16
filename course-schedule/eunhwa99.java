import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {

  // TC: O(numCourses + E) E는 prerequisites 배열의 길이 (즉, 간선의 개수).
  // SC: O(numCourses + E)
  public boolean canFinish(int numCourses, int[][] prerequisites) {
    int[] inDegree = new int[numCourses];
    List<List<Integer>> adj = new ArrayList<>();

    for (int i = 0; i < numCourses; i++) {
      adj.add(new ArrayList<>());
    }

    for (int[] pre : prerequisites) {
      adj.get(pre[1]).add(pre[0]);
      inDegree[pre[0]]++;
    }

    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
      if (inDegree[i] == 0) {
        queue.add(i);
      }
    }
    for (int i = 0; i < numCourses; i++) {
      if (queue.isEmpty()) {
        return false;
      }
      int course = queue.poll();

      for (int nextCourse : adj.get(course)) {
        inDegree[nextCourse]--;
        if (inDegree[nextCourse] == 0) {
          queue.add(nextCourse);
        }
      }
    }
    return queue.isEmpty();
  }
}

