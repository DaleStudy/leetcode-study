class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        /**
        1.문제: [a, b] = b를 수강해야 a 수강 가능, 모두 수강가능하면 true, 아니면 flase return
        2.constraints
        - numCourses min = 1, max = 2000
        - prerequisites length min = 0, max = 5000
        3.solution
        - dfs, graph에 cycle 이 존재하는지 check. cycle 이 존재하면 수강 다 못하므로 false return
         */
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        //graph 생성
        for(int i = 0; i < prerequisites.length; i++) {
            int a = prerequisites[i][0];
            int b = prerequisites[i][1];

            graph.get(b).add(a);
        }

        //dfs cycle check
        //state: 0 = 방문 전, 1 = 방문 중, 2 = 방문 완료
        int[] state = new int[numCourses];
        //node 개수(numCourses)만큼 순회
        for(int i = 0; i < numCourses; i++) {
            //cycle 존재하면 false return
            if(dfs(i, graph, state)) {
                return false;
            }
        }
        return true;
    }

     
    boolean dfs(int i, List<List<Integer>> graph, int[] state) {
        //순회 cycle 발견하면 true
        if(state[i] == 1) {
            return true;
        }
        if(state[i] == 2) {
            return false;
        }
        state[i] = 1;

        for(int next: graph.get(i)) {
            if(dfs(next, graph, state)) {
                return true;
            }
        }
        state[i] = 2;
        return false;
    }
}
