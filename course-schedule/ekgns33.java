/*
*
* solution : topological sort
* tc : O(E + V)
* sc : O(E + V)
*
* */
class Solution {
  public boolean canFinish(int numCourses, int[][] prerequisites) {
    List<Integer>[] adj = new ArrayList[numCourses];
    for(int i = 0 ; i < numCourses; i++) {
      adj[i] = new ArrayList<>();
    }
    boolean[] v = new boolean[numCourses];
    int[] indeg = new int[numCourses];
    for(int[] pre : prerequisites) {
      int src = pre[0];
      int dst = pre[1];
      adj[src].add(dst);
      indeg[dst]++;
    }
    Queue<Integer> q = new LinkedList<>();
    for(int i = 0; i < numCourses; i ++) {
      if(indeg[i] == 0) {
        q.add(i);
        v[i] = true;
      }
    }
    int cnt= 0;
    while(!q.isEmpty()) {
      int curNode = q.poll();
      cnt++;
      for(int dst : adj[curNode]) {
        indeg[dst]--;
        if(indeg[dst] ==0 && !v[dst]) {
          q.add(dst);
        }
      }
    }

    return cnt == numCourses;

  }
}
