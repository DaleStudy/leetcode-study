import java.util.*;

public class Geegong {

    /**
     * in-degree array, graph, queue 이용
     * directed acyclic graph (DAG) 문제..
     * in-degree array : 타 노드에서 유입이 되는 갯수
     * graph : [a,b] 이렇게 있으면 b -> a 로 가는 방향 edge 를 표현
     * queue : in-degree array 에서 0 인 노드들. 즉 바로 수강할 수 있는 녀석들을 차례차례 넣어 카운팅할 예정
     * (예전에도 동일하게 풀어서 .. 한번 더 복습하는 느낌으로 풀었습니다)
     * @param numCourses
     * @param prerequisites
     * @return
     */
    public boolean canFinish(int numCourses, int[][] prerequisites) {

        int[] indegreeCnt = new int[numCourses];
        List<List<Integer>> outdegree = new ArrayList<>();
        // set outdegree
        for (int idx=0; idx<numCourses; idx++) {
            outdegree.add(new ArrayList<>());
        }

        // set indgree, outdegree, candidateNoIndgree
        for (int[] pre : prerequisites) {
            int course = pre[0];
            int prerequisite = pre[1];

            if (course == prerequisite) {
                return false;
            }

            outdegree.get(prerequisite).add(course);
            indegreeCnt[course]++;
        }

        // find indgree zero
        Queue<Integer> queue = new ArrayDeque<>();
        for (int idx=0; idx<numCourses; idx++) {
            if (indegreeCnt[idx] == 0) {
                queue.add(idx);
            }
        }


        int currentTakenCnt = 0;
        while(!queue.isEmpty()) {
            int indegreeZero = queue.poll();
            currentTakenCnt++;

            List<Integer> targets = outdegree.get(indegreeZero);
            for (int course : targets) {
                indegreeCnt[course]--;
                if (indegreeCnt[course] == 0) {
                    queue.add(course);
                }
            }
        }

        return currentTakenCnt == numCourses;
    }

}
