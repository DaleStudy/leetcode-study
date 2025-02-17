// 사이클을 찾는 문제. DFS를 이용해서 방문했는지 여부를 관리하고 체크하면된다.
// DFS를 진행 중인 것을 들고 있어야 사이클 여부를 판단할 수 있다.
// 간선 수와 노드의 수에 따라 시간 복잡도가 결정됨 O(N+L)
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] pair : prerequisites) {
            graph.get(pair[1]).add(pair[0]);
        }

        // 0: 방문 X
        // -1: DFS 진행 중
        // 1: 방문 완료
        int[] visited = new int[numCourses];

        // 모든 노드에서 DFS 수행
        for (int i = 0; i < numCourses; i++) {
            if (dfs(graph, visited, i)) return false;
        }
        
        return true;
    }

    private boolean dfs(List<List<Integer>> graph, int[] visited, int node) {
        if (visited[node] == -1) return true;  // 방문 중이면 사이클이 발견
        if (visited[node] == 1) return false; 

        visited[node] = -1; // 진행 중 표기
        for (int next : graph.get(node)) {
            if (dfs(graph, visited, next)) return true;
        }
        visited[node] = 1;

        return false;
    }
}
