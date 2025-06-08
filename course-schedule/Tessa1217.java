import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // return BFS(numCourses, prerequisites);
        return DFS(numCourses, prerequisites);
    }

    // BFS 방식으로 풀이
    private boolean BFS(int numCourses, int[][] prerequisites) {

        // 연결 그래프 생성
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        // 들어오는 간선의 수 배열
        int[] inDegree = new int[numCourses];

        for (int[] pre : prerequisites) {
            int course = pre[0];
            int prereq = pre[1];
            inDegree[course]++;
            graph.get(prereq).add(course);
        }

        // 들어오는 간선이 없는 과목 Queue에 삽입
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < inDegree.length; i++) {
            if (inDegree[i] == 0) {
                q.offer(i);
            }
        }

        // 들은 과목 수
        int takeCourse = 0;
        while (!q.isEmpty()) {
            int course = q.poll();
            takeCourse++;

            for (int connect : graph.get(course)) {
                inDegree[connect]--;
                if (inDegree[connect] == 0) {
                    q.offer(connect);
                }
            }
        }

        return takeCourse == numCourses;
    }

    // DFS 방식 풀이
    private boolean DFS(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] pre : prerequisites) {
            int course = pre[0];
            int prereq = pre[1];
            graph.get(prereq).add(course);
        }

        // 처리 상태 배열
        int[] state = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            if (hasCycle(graph, state, i)) {
                return false;
            }
        }

        return true;
    }

    // 사이클 여부 확인
    private boolean hasCycle(List<List<Integer>> graph, int[] state, int course) {

        if (state[course] == 1) return true; // 사이클이 있다면
        if (state[course] == 2) return false; // 이미 처리 완료되었으므로 return

        state[course] = 1;
        for (int connect : graph.get(course)) {
            if (hasCycle(graph, state, connect)) {
                return true;
            }
        }
        state[course] = 2; // 처리 완료
        return false;
    }
}

